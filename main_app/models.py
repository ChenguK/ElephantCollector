from django.db import models


# Create your models here.



class Elephant(models.Model): 
    name = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=200)
    species = models.CharField(max_length=100)
    sex = models.CharField(max_length=50)
    fictional = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    dod = models.CharField(max_length=50)
    wikilink = models.URLField(max_length=100)
    image = models.ImageField(width_field=100)
    note = models.TextField(max_length=300)