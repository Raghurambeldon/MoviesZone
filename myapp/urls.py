from django.urls import path
from . import views

urlpatterns = [
  
    path('',views.Home_view,name='home'),
    path('movies/',views.Movies_view,name='moviespage'),
    path('movies/<str:name>/',views.Movie_display,name='Movie_display'),
    path('series/',views.Series_view,name='seriespage'),
    path('newreleases/',views.Newreleases_view,name='newreleases')
]