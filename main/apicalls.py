import requests
import xml.etree.ElementTree as ET


def search_stackoverflow(request):
	location = request.GET['search']
	resp = requests.get('https://stackoverflow.com/jobs/feed', params={'location': location})
	root = ET.fromstring(resp.content)
	
	techs = {}
	job_posts = [x for x in root[0] if x.tag == 'item']
	for post in job_posts:
		categories = [x for x in post if x.tag == 'category']
		for category in categories:
			try: 
				techs[category.text] += 1
			except KeyError:
				techs[category.text] = 1
	return techs