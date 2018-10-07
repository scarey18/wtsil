from django.shortcuts import render

from .apicalls import run_searches


def home(request):
	search = request.GET.get('search', '')
	if search != '':
		results = run_searches(request)
		context = {'search': search, 'results': results}
		return render(request, 'main/search.html', context)
	return render(request, 'main/home.html')
