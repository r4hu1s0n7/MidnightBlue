from django.http.response import Http404
from django.shortcuts import render
from MidnightBlue.models import *
from datetime import date
from django_pandas.io import read_frame
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
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

def movieinfo(request,id):
	qs = MovieDB.objects.filter(imdb_id__icontains=id)
	if not qs:
		raise Http404()
	context = {'data':qs, 'year':date.today().year}
	return render(request, 'moviesingle.html', context)

def searchMovie(request):
	if 'term' in request.GET:
		qs = MovieDB.objects.filter(title__icontains=request.GET.get('term')) | MovieDB.objects.filter(genres__icontains=request.GET.get('term')) | MovieDB.objects.filter(cast__icontains=request.GET.get('term')) | MovieDB.objects.filter(director__icontains=request.GET.get('term')) | MovieDB.objects.filter(keywords__icontains=request.GET.get('term'))
		titles = list()
		for product in qs:
			titles.append(product.original_title)
		return JsonResponse(titles, safe=False)
	z=0
	context={'year':date.today().year}
	k = request.GET.get('sch')
	if k:
		qs = MovieDB.objects.filter(title__icontains=k) | MovieDB.objects.filter(genres__icontains=k) | MovieDB.objects.filter(cast__icontains=k) | MovieDB.objects.filter(director__icontains=k) | MovieDB.objects.filter(keywords__icontains=k)
		context = {'data':qs,'year':date.today().year,'count':qs.count(), 'k':k}
	else:
		context = {'year':date.today().year,'count':0, 'k':k}
	return render(request,'search.html',context)

def recommendation(request):
	movie = request.GET.get('sch')
	context = {}
	print(movie,'-')
	if movie:
		context = recommend(movie)
	return render(request,'recommendation.html', context)

def recommend(need):
	z=0
	qs = MovieDB.objects.all()
	df = read_frame(qs)
	indeces = [x for x in range(4803)]
	df['index'] = indeces

	def get_title_from_index(index):
		return df[df.index == index]["original_title"].values[0]
	
	def get_index_from_title(title):
		print(title)
		k = df[df.original_title == title]["index"].values[0]
		print(k)
		return k
	
	feature = ['keywords','cast','genres','director']
	for f in feature:
		df[f] = df[f].fillna('')
	
	def combine_features(row):
		try:
			return str(row['keywords']) + " " + str(row['cast']) + " " + str(row["genres"]) + " " + str(row['director'])
		except:
			print("Error",row)
	
	df["combined_features"] = df.apply(combine_features,axis=1)
	
	cv = CountVectorizer()
	count_matrix = cv.fit_transform(df["combined_features"] )
	cos_sim = cosine_similarity(count_matrix)
	
	movie_user_likes = need
	movie_index = get_index_from_title(movie_user_likes)
	print(movie_index)
	
	similar_movies = list(enumerate(cos_sim[movie_index]))
	sorted_similar = sorted(similar_movies,key =  lambda x:x[1] , reverse=True)
	curr = df[df.index == sorted_similar[0][0]]["vote_average"].values
	curr = int(curr)
	minList = []
	cnt=0
	
	for i in sorted_similar:
		movieRating = int(df[df.index == i[0]]["vote_average"].values)
		x = curr - 1
		y = curr + 1
		name = get_title_from_index(i[0])
		if movieRating in range(x,11) and name not in minList:
			minList.append(name)
			cnt+=1
			print(movieRating)
		if cnt == 37:
			break	
	print(minList)
	imdb,names,poster,rating = [],[],[],[]
	for k in minList:
		if k.find('?') > -1:
			continue
		try:
			names.append(df[df['original_title'].str.contains(k,case=False,na=False,regex=False)]['original_title'].values[0])
			poster.append(df[df['original_title'].str.contains(k,case=False,na=False,regex=False)]['poster'].values[0])
			imdb.append(df[df['original_title'].str.contains(k,case=False,na=False,regex=False)]['imdb_id'].values[0])
			rating.append(df[df['original_title'].str.contains(k,case=False,na=False,regex=False)]['vote_average'].values[0])
		except Exception as e:
			print(e)	
	z = len(names)

	context = {'data':zip(names, poster, imdb, rating),'count':z,'year':date.today().year, 'k':need}
	return context

def moviegridfw(request):
	return render(request, 'moviegridfw.html')

def profile(request):
	return render(request, 'userprofile.html')

def userfav(request):
	queryset = MovieDB.objects.filter(first_name__startswith='R') | MovieDB.objects.filter(last_name__startswith='D')
	return render(request, 'userfavoritegrid.html')

def error_404(request, exception):
	return render(request,'404.html')

def error_500(request, *args, **argv):
	return render(request,'500.html')
