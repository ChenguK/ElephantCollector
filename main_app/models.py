from django.db import models
from django.urls import reverse
from datetime import date
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.


SPECIES = (
    ('1', 'African'),
    ('2', 'Asian'),
)

SEX = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('U', 'Unknown'),
)

SERVICES = (
    ('O', 'Oral Hygiene'),
    ('F', 'Checked Feet'),
    ('E', 'Exercise'),
)

class Trainer(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('trainers_detail', kwargs={ 'trainer_id': self.id})


class Elephant(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    affiliation = models.CharField(max_length=200, help_text=_("Please Enter the Person or Company with whom they were most Affiated."))
    species = models.CharField(
        max_length=1,
        choices=SPECIES,
        default=SPECIES[0][0],
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX,
        default=SEX[0][0],
    )
    birthdate = models.CharField(max_length=50, help_text=_("Please enter the Elephant's Birth Year or 'Unknown'")) 
    died = models.CharField(max_length=50, help_text=_("Please enter the Year the Elephant Died, 'Unknown' or 'Alive'"))
    wikilink = models.URLField(max_length=200)
    note = models.TextField(max_length=500)
    trainers = models.ManyToManyField(Trainer)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail', kwargs={'elephant_id': self.id })

    def has_elephants(self):
        return self.elephant_set

    def cared_for_today(self):
        return self.care_set.filter(date=date.today()).count() >= len(SERVICES)
        
    class Meta:
        ordering = ['name']
 
class Care(models.Model):
    date = models.DateField('care date')
    service = models.CharField(
        max_length=1,
        choices=SERVICES,
        default=SERVICES[0][0],
    )
    elephant = models.ForeignKey(Elephant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_service_display()} on {self.date}'

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    elephant = models.ForeignKey(Elephant, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for elephant_id: {self.elephant_id} @{self.url}'

