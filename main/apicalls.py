import requests
import xml.etree.ElementTree as ET

from .techlist import TechCounter, TECHS


def search_all_sites(request):
	return aggregate_results([
		search_stackoverflow(request),
	])

def aggregate_results(search_results):
	categories = {
		'Languages': [],
		'Frameworks/CMS': [],
		'Platforms/Web Services': [],
		'Libraries/Tools': [],
		'Game Engines': [],
		'Concepts/Skills': [],
		'Operating Systems': [],
		'Databases': [],
		'Other uncategorized keywords': [],
	}
	for results in search_results:
		for key in results:
			match = False
			for tech in TECHS:
				if tech.match(key):
					tech.count += results[key]
					match = True
					if tech not in categories[tech.category]:
						categories[tech.category].append(tech)
			if not match:
				new_tech = TechCounter(key, create_regex(key), 'Other uncategorized keywords', count=results[key])
				categories['Other uncategorized keywords'].append(new_tech)
				TECHS.append(new_tech)

	for c in categories:
		categories[c] = sorted(categories[c], key=lambda tech: -tech.count)

	return categories

def create_regex(string):
	tokens = '-.?+*,$'
	regex = r'^'
	for char in string:
		if char in tokens:
			regex += f'\{char}'
		else:
			regex += char
	return regex + '$'

def search_stackoverflow(request):
	location = request.GET['search']
	resp = requests.get('https://stackoverflow.com/jobs/feed', params={'location': location})
	root = ET.fromstring(resp.content)
	
	keywords = {}
	job_posts = [x for x in root[0] if x.tag == 'item']
	for post in job_posts:
		categories = [x for x in post if x.tag == 'category']
		for category in categories:
			try: 
				keywords[category.text] += 1
			except KeyError:
				keywords[category.text] = 1
	return keywords