from django.test import TestCase
from django.urls import reverse


class ViewsTest(TestCase):
	def test_home_view(self):
		url = reverse('main:home')
		resp = self.client.get(url)
		self.assertContains(resp, 'What Technology Should I Learn')

	def test_results_view(self):
		url = reverse('main:home') + '/?search=New+York%2C+NY%2C+USA'
		resp = self.client.get(url)
		self.assertContains(resp, 'Results for New York, NY, USA')