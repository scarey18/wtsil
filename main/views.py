from django.shortcuts import render

from .apicalls import search_all_sites


def home(request):
	search = request.GET.get('search', '')
	if search != '':
		results = search_all_sites(request)
		context = {'search': search, 'results': results}
		return render(request, 'main/search.html', context)
	return render(request, 'main/home.html')
