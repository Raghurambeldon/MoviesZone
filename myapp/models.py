from django.db import models

# Create your models here.
class Movie(models.Model):

    Genre_Choices = [
                     ('Horror','Horror'),
                     ('action','action'),
                     ('romance','romance'),
                     ('thriller','thriller'),
                     ('drama','drama'),
                     ('other','other')
                     ]
    
    Language_choices = [
                     ('telugu','telugu'),
                     ('english','english'),
                     ('hindi','hindi'),
                     ('tamil','tamil'),
                     ('kannada','kannada'),
                     ('other','other')
                     
    ]
    
    name = models.CharField(max_length=50)
    cast = models.TextField(max_length=50)
    director = models.CharField(max_length=20)
    synopsis = models.TextField(max_length=150)
    Rating = models.FloatField(max_length=10)   
    Is_Trending = models.BooleanField(default=False)
    Is_Toprated = models.BooleanField(default=False)
    Is_Newreleased = models.BooleanField(default=False)
    language = models.CharField( max_length=50,choices=Language_choices,null=True,blank=True)
    genre = models.CharField( max_length=50,choices=Genre_Choices,default='action')
    poster = models.ImageField(upload_to='posters')
    moviefile = models.FileField( upload_to='moviefile',null=True,blank=True )
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name