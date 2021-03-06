from django.http.response import Http404
from django.shortcuts import render
from MidnightBlue.models import *
from datetime import date
from django.http import JsonResponse
from .forms import *

def index(request):
	mainslidebar_movies = ['Avatar','Me Before You', 'The Notebook']
	mainslidebar_row = get_movie(mainslidebar_movies)

	trending_movies = ['Interstellar', 'The Notebook', 'Django Unchained', 'Midnight in Paris', 'The Dark Knight', 'Before Sunrise', 'The Grand Budapest Hotel', 'The Prestige']
	trending_row = get_movie(trending_movies)
		
	editors_movie = ['Me Before You', 'The Notebook', 'Interstellar', 'Shutter Island', 'The Dark Knight', 'The Shawshank Redemption', 'The Imitation Game', 'The Pursuit of Happyness']
	editor_row = get_movie(editors_movie)

	context = {'trending':trending_row,'editor':editor_row,'main':mainslidebar_row,'year':date.today().year}
	
	return render(request, 'index.html', context)

def get_movie(keys):
	qs = MovieDB.objects.filter(original_title__in=keys)
	return qs

def about(request):
	return render(request, 'about.html')

def autocomplete(request):
    if 'term' in request.GET:
        qs = MovieDB.objects.filter(title__icontains=request.GET.get('term')) | MovieDB.objects.filter(genres__icontains=request.GET.get('term')) | MovieDB.objects.filter(cast__icontains=request.GET.get('term')) | MovieDB.objects.filter(director__icontains=request.GET.get('term')) | MovieDB.objects.filter(keywords__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.original_title)
        return JsonResponse(titles, safe=False)
    return render(request, 'test_search.html')

def moviegridfw(request):
	return render(request, 'moviegridfw.html')

def movieinfo(request,id):
	qs = MovieDB.objects.filter(imdb_id__icontains=id)
	if not qs:
		raise Http404()
	context = {'data':qs, 'year':date.today().year}
	return render(request, 'moviesingle.html', context)

def profile(request):
	return render(request, 'userprofile.html')

def userfav(request):
	queryset = MovieDB.objects.filter(first_name__startswith='R') | MovieDB.objects.filter(last_name__startswith='D')
	return render(request, 'userfavoritegrid.html')

def searchMovie(request):
	z=0
	context={'year':date.today().year}
	k = request.GET.get('sch')
	if k:
		qs = MovieDB.objects.filter(title__icontains=k) | MovieDB.objects.filter(genres__icontains=k) | MovieDB.objects.filter(cast__icontains=k) | MovieDB.objects.filter(director__icontains=k) | MovieDB.objects.filter(keywords__icontains=k)
		context = {'data':qs,'year':date.today().year,'count':qs.count(), 'k':k}
	return render(request,'search.html',context)

def error_404(request, exception):
	return render(request,'404.html')

def error_500(request, *args, **argv):
	return render(request,'500.html')