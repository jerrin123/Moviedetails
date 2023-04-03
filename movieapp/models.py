from django.db import models

# Create your models here.\
class Movie(models.Model):
    title=models.CharField(max_length=300)
    language=models.CharField(max_length=300)
    director=models.CharField(max_length=300)
    actror=models.CharField(max_length=300)
    actress=models.CharField(max_length=300)
    release=models.DateField("Release Date")
    status=models.CharField(max_length=300)
