from django.shortcuts import render

from .apicalls import search_stackoverflow


def home(request):
	search = request.GET.get('search', '')
	if search != '':
		results = search_stackoverflow(request)
		techs = [f'{r}: {results[r]}' for r in results]
		context = {'techs': techs, 'search': search}
		return render(request, 'main/search.html', context)
	return render(request, 'main/home.html')
