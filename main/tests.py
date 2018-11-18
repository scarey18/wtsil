from django.test import TestCase
from django.urls import reverse

import asyncio

from .apicalls import *


class ViewsTest(TestCase):
	def test_home_view(self):
		url = reverse('main:home')
		resp = self.client.get(url)
		self.assertContains(resp, 'What Technology Should I Learn')

	def test_results_view(self):
		url = reverse('main:home') + '/?search=New+York%2C+NY%2C+USA'
		resp = self.client.get(url)
		self.assertContains(resp, 'Results for New York, NY, USA')
		self.assertFalse(resp.context['no_results'])


class ApicallsTest(TestCase):
	def test_search_all(self):
		search = 'New York, NY, USA'
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		results = loop.run_until_complete(search_all(loop, search))
		for r in results:
			self.assertTrue(type(r['results']) is list)
			self.assertTrue(r['status'] == 200)