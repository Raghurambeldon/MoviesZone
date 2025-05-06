from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie
# Create your views here.

def Home_view(request):
    movies = Movie.objects.all()
    telugu_movies = Movie.objects.filter(language='telugu')
    top_rated = Movie.objects.filter(Is_Toprated='True')
    created_at = Movie.objects.latest('created_at')
    return render(request,'homepage.html',{'movies':movies,'telugumovies':telugu_movies,'toprated':top_rated,'created_at':created_at})


def Movies_view(request):
    movies = Movie.objects.all()
    return render(request,'movies.html',{'movies':movies})


def Movie_display(request,name):
    movies = get_object_or_404(Movie,name=name)
    return render(request,'moviedisplay.html',{'movies':movies})


def Series_view(request):
    return render(request,'series.html')


def Newreleases_view(request):
    movies = Movie.objects.all()
    return render(request,'newreleases.html',{'movies':movies})
