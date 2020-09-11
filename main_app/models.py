from django.db import models
from django.urls import reverse


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
    image = models.ImageField(upload_to='main_app/static/images')
    note = models.TextField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'elephant_id': self.id })
 