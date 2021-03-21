from django.urls import path
from django.conf.urls import url
from . import views

handler404 = 'MidnightBlue.views.error_404'
handler500 = 'MidnightBlue.views.error_500'

urlpatterns = [
	path('', views.index, name="index"),
	path('search', views.searchMovie, name="search"),
	path('moviesingle/<str:id>', views.movieinfo, name="movieinfo"),
	path('moviegridfw', views.moviegridfw, name="moviegridfw"),
	path('userprofile', views.profile, name="profile"),
	path('userfavoritegrid', views.userfav, name="userfav"),
    path('suggest', views.suggest, name="suggest"),
	path('recommendation', views.recommendation),
	path('test', views.test),

]
