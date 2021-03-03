from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('search', views.searchMovie, name="search"),
	path('moviesingle/<str:id>', views.movieinfo, name="movieinfo"),
	path('moviegridfw', views.moviegridfw, name="moviegridfw"),
	path('userprofile', views.profile, name="profile"),
	path('userfavoritegrid', views.userfav, name="userfav"),
    path('about', views.about, name="about"),
	path('testsearch', views.autocomplete, name='autocomplete'),
]
