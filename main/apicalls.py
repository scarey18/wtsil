import xml.etree.ElementTree as ET
import aiohttp
import asyncio
import os

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


def run_searches(request):
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	results = loop.run_until_complete(search_all(loop, request))
	return aggregate_results(results)

async def search_all(loop, request):
	searches = [
		search_stackoverflow,
		search_github,
		search_authentic_jobs,
	]
	async with aiohttp.ClientSession(loop=loop) as session:
		results = [search(session, request) for search in searches]
		return await asyncio.gather(*results)

async def search_stackoverflow(session, request):
	location = request.GET['search']
	base_url = 'https://stackoverflow.com/jobs/feed'
	async with session.get(base_url, params={'location': location}) as resp:
		root = ET.fromstring(await resp.text())
		categories = {category:[] for category in CATEGORIES}
		job_posts = [x for x in root[0] if x.tag == 'item']
		for post in job_posts:
			keywords = [x for x in post if x.tag == 'category']
			for keyword in keywords:
				categories = find_match(categories, keyword.text)
		return categories

async def search_github(session, request):
	location = request.GET['search']
	base_url = 'https://jobs.github.com/positions.json'
	async with session.get(base_url, params={'location': location}) as resp:
		results = await resp.json()
		categories = {category:[] for category in CATEGORIES}
		for post in results:
			categories = find_match(categories, post['description'], create_new=False)
		return categories

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
		results = await resp.json()
		categories = {category:[] for category in CATEGORIES}
		for post in results['listings']['listing']:
			categories = find_match(categories, post['title'], create_new=False)
			categories = find_match(categories, post['description'], create_new=False)
		return categories

def find_match(categories, text, create_new=True):
	match = False
	techs = new_tech_list()
	for tech in techs:
		if tech.match(text):
			tech.count += 1
			match = True
			if tech not in categories[tech.category]:
				categories[tech.category].append(tech)
	if not match and create_new:
		new_tech = TechCounter(text, create_regex(text), 'Other uncategorized keywords', count=1)
		categories['Other uncategorized keywords'].append(new_tech)
		techs.append(new_tech)
	return categories

def aggregate_results(search_results):
	categories = {category:[] for category in CATEGORIES}
	for results in search_results:
		for key in results:
			for tech in results[key]:
				shared_techs = [t for t in categories[key] if t.name == tech.name]
				if len(shared_techs) == 0:
					categories[key].append(tech)
				else:
					shared_techs[0].count += tech.count
	for key in categories:
		categories[key] = sorted(categories[key], key=lambda tech: -tech.count)
		if key != 'Other uncategorized keywords':
			max_count = max((tech.count for tech in categories[key])) if len(categories[key]) > 0 else None
			for tech in categories[key]:
				percent = int((tech.count / max_count) * 100)
				tech.graph_percentage = f'{percent}%' if percent > 0 else '1%'
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