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


def run_searches(search):
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	results = loop.run_until_complete(search_all(loop, search))
	return aggregate_results(sorted(results, key=lambda r: -r['create_new']))


async def search_all(loop, search):
	async with aiohttp.ClientSession(loop=loop) as session:
		return await asyncio.gather(
			asyncio.ensure_future(search_stackoverflow(session, search)),
			asyncio.ensure_future(search_github(session, search)),
		)


async def search_stackoverflow(session, search):
	base_url = 'https://stackoverflow.com/jobs/feed'
	async with session.get(base_url, params={'location': search}) as resp:
		results_dict = {'results': [], 'create_new': True, 'status': resp.status}
		if resp.status != 200:
			print(resp)
			return results_dict
		root = ET.fromstring(await resp.text())
		job_posts = [x for x in root[0] if x.tag == 'item']
		for post in job_posts:
			results_dict['results'] += [x.text for x in post if x.tag == 'category']
		print('Stackoverflow: done')
		print(f'Number of results: {len(job_posts)}')
		return results_dict


async def search_github(session, search):
	base_url = 'https://jobs.github.com/positions.json'
	async with session.get(base_url, params={'location': search}) as resp:
		results_dict = {'results': [], 'create_new': True, 'status': resp.status}
		if resp.status != 200:
			print(resp)
			return results_dict
		json = await resp.json()
		results_dict['results'] = [parse_html(post['description']) for post in json]
		print('Github: done')
		print(f'Number of results: {len(results_dict["results"])}')
		return results_dict


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
