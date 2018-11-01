from django.shortcuts import render
from django.core.cache import cache
import time

from .apicalls import run_searches


def home(request):
	search = request.GET.get('search', '')
	if search != '':
		start = time.time()
		results = cache.get(search)
		if results is None:
			print('Making API calls')
			results = run_searches(request)
			cache.set(search, results, 60 * 60 * 12)
		else:
			print('Retrieved from cache')
		no_results = max((len(results[x]) for x in results)) == 0
		context = {'search': search, 'results': results, 'no_results': no_results}
		print(time.time() - start)
		return render(request, 'main/search.html', context)
	return render(request, 'main/home.html')