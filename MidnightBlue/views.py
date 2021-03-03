from django.shortcuts import render
from MidnightBlue.models import *
from django_pandas.io import read_frame
from datetime import date
from django.http import JsonResponse
from .forms import *

def index(request):
	mainslidebar_movies = 'Avatar'
	mainslidebar_row = get_main_movie(mainslidebar_movies)

	trending_movies = ['Interstellar', 'The Notebook', 'Django Unchained', 'Midnight in Paris', 'The Dark Knight', 'Before Sunrise', 'The Grand Budapest Hotel', 'The Prestige']
	trending_row = get_movie(trending_movies)
		
	editors_movie = ['Me Before You', 'The Notebook', 'Interstellar', 'Shutter Island', 'The Dark Knight', 'The Shawshank Redemption', 'The Imitation Game', 'The Pursuit of Happyness']
	editor_row = get_movie(editors_movie)

	context = {'trending':trending_row,'editor':editor_row,'main':mainslidebar_row,'year':date.today().year}
	
	return render(request, 'index.html', context)

def get_movie(keys):
	qs = MovieDB.objects.all()
	d = read_frame(qs)
	imdb,names,poster,rating = [],[],[],[]
	for k in keys:
		try:
			imdb.append(d[d['original_title'].str.contains(k,case=False,na=False)]['imdb_id'].values[0])
			poster.append(d[d['original_title'].str.contains(k,case=False,na=False)]['poster'].values[0])
			rating.append(d[d['original_title'].str.contains(k,case=False,na=False)]['vote_average'].values[0])
			names.append(d[d['original_title'].str.contains(k,case=False,na=False)]['original_title'].values[0])
		except:
			print(k)
	return zip(imdb,poster,rating,names)

def get_main_movie(keys):
	qs = MovieDB.objects.filter(original_title=keys)
	return qs

def about(request):
	return render(request, 'about.html')

def autocomplete(request):
    if 'term' in request.GET:
        qs = MovieDB.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.original_title)
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    return render(request, 'test_search.html')

def moviegridfw(request):
	return render(request, 'moviegridfw.html')

def movieinfo(request,id):
	qs = MovieDB.objects.filter(imdb_id__icontains=id)
	context = {'data':qs, 'year':date.today().year}
	return render(request, 'moviesingle.html', context)

def profile(request):
	return render(request, 'userprofile.html')

def userfav(request):
	return render(request, 'userfavoritegrid.html')

def searchMovie(request):
	z=0
	qs = MovieDB.objects.all()
	d = read_frame(qs)
	k = request.GET.get('sch')
	imdb,names,poster,rating = [],[],[],[]
	try:
		imdb = list(d[d['original_title'].str.contains(k,case=False,na=False)]['imdb_id'].values)
		poster = list(d[d['original_title'].str.contains(k,case=False,na=False)]['poster'].values)
		rating = list(d[d['original_title'].str.contains(k,case=False,na=False)]['vote_average'].values)
		names = list(d[d['original_title'].str.contains(k,case=False,na=False)]['original_title'].values)
	except Exception as e:
		print("e=",e)
	z = len(names)
	context = {'data':zip(imdb,poster,rating,names),'year':date.today().year,'count':z}
	return render(request,'search.html',context)