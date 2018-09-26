from django.shortcuts import render

from .apicalls import search_all_sites


def home(request):
	search = request.GET.get('search', '')
	if search != '':
		context = search_all_sites(request)
		context.update({'search': search})
		return render(request, 'main/search.html', context)
	return render(request, 'main/home.html')
