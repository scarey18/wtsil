from django.shortcuts import render
from django.core.cache import cache

from .apicalls import run_searches


def home(request):
	search = request.GET.get('search', '')
	if search != '':
		results = cache.get(search)
		if results is None:
			print('Making API calls')
			results = run_searches(request)
			cache.set(search, results, 60 * 60 * 12)
		else:
			print('Retrieved from cache')
		template = 'main/search.html' if max((len(results[x]) for x in results)) > 0 else 'main/no_results.html'
		context = {'search': search, 'results': results}
		return render(request, template, context)
	return render(request, 'main/home.html')