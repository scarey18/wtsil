import xml.etree.ElementTree as ET
import aiohttp
import asyncio
import os
import re

from .techlist import TechCounter, new_tech_list


CATEGORIES = [
	'Languages',
	'Frameworks/CMS',
	'Platforms/Web Services',
	'Libraries/Tools',
	'Game Engines',
	'Concepts/Skills',
	'Operating Systems',
	'Databases',
	'Other uncategorized keywords',
]

SPLIT_REGEX = re.compile(r'<.+?>')

UNWANTED_TEXT = ['', '\n']


def run_searches(request):
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	results = loop.run_until_complete(search_all(loop, request))
	return aggregate_results(sorted(results, key=lambda r: -r['create_new']))

async def search_all(loop, request):
	async with aiohttp.ClientSession(loop=loop) as session:
		return await asyncio.gather(
			asyncio.ensure_future(search_stackoverflow(session, request)),
			asyncio.ensure_future(search_github(session, request)),
			# asyncio.ensure_future(search_authentic_jobs(session, request)),
		)

async def search_stackoverflow(session, request):
	location = request.GET['search']
	base_url = 'https://stackoverflow.com/jobs/feed'
	async with session.get(base_url, params={'location': location}) as resp:
		if resp.status != 200:
			print(resp)
			return {}
		results = []
		root = ET.fromstring(await resp.text())
		job_posts = [x for x in root[0] if x.tag == 'item']
		for post in job_posts:
			results += [x.text for x in post if x.tag == 'category']
		print('Stackoverflow: done')
		print('Number of results: ' + str(len(job_posts)))
		return {'results': results, 'create_new': True}

async def search_github(session, request):
	location = request.GET['search']
	base_url = 'https://jobs.github.com/positions.json'
	async with session.get(base_url, params={'location': location}) as resp:
		if resp.status != 200:
			print(resp)
			return {}
		json = await resp.json()
		results = [parse_html(post['description']) for post in json]
		print('Github: done')
		print('Number of results: ' + str(len(results)))
		return {'results': results, 'create_new': False}

async def search_authentic_jobs(session, request):
	base_url = 'https://authenticjobs.com/api/'
	params = {
		'api_key': os.environ['AUTH_JOBS_KEY'],
		'method': 'aj.jobs.search',
		'format': 'json',
		'location': request.GET['search'],
		'perpage': '100',
	}
	async with session.get(base_url, params=params) as resp:
		if resp.status != 200:
			print(resp)
			return {}
		json = await resp.json()
		results = []
		for post in json['listings']['listing']:
			results.append(parse_html(post['description']))
		print('Authentic jobs: done')
		print('Number of results: ' + str(len(results)))
		return {'results': results, 'create_new': False}

def parse_html(html):
	split_html = re.split(SPLIT_REGEX, html)
	trimmed = [t for t in split_html if t not in UNWANTED_TEXT and not t.startswith('&')]
	return ', '.join(trimmed)

def aggregate_results(results):
	categories = {category:[] for category in CATEGORIES}
	techs = new_tech_list()
	for r in results:
		for text in r['results']:
			categories = find_match(categories, techs, text, r['create_new'])
	for key in categories:
		categories[key] = sorted(categories[key], key=lambda tech: -tech.count)
		if key != 'Other uncategorized keywords':
			max_count = max((tech.count for tech in categories[key])) if len(categories[key]) > 0 else None
			for tech in categories[key]:
				percent = int((tech.count / max_count) * 100)
				tech.graph_percentage = f'{percent}%' if percent > 0 else '1%'
	return categories

def find_match(categories, techs, text, create_new):
	match = False
	for tech in techs:
		if tech.match(text):
			tech.count += 1
			match = True
			if tech.count == 1:
				categories[tech.category].append(tech)
	if not match and create_new:
		new_tech = TechCounter(text, create_regex(text), 'Other uncategorized keywords', count=1)
		categories['Other uncategorized keywords'].append(new_tech)
		techs.append(new_tech)
	return categories

def create_regex(string):
	tokens = '-.?+*,$'
	regex = r''
	for char in string:
		if char in tokens:
			regex += f'\{char}'
		else:
			regex += char
	return regex
