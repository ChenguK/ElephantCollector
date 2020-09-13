from django.db import models
from django.urls import reverse


# Create your models here.

BIRTH = (
    ('U', 'Unknown'),
    ('D', 'Year'),
)

DEATH = (
    ('U', 'Unknown'),
    ('D', 'Year'),
    ('A', 'Alive'),
 )

SEX = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('U', 'Unknown')
)

CARE = (
    ('O', 'Oral Hygiene'),
    ('F', 'Foot Care'),
    ('E', 'Exercise'),
)



class Elephant(models.Model):
    name = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=200)
    species = models.CharField(max_length=100)
    sex = models.CharField(
        max_length=1,
        choices=SEX,
        default=SEX[0][0],
    )
    birthdate = models.CharField(
        max_length=1,
        choices=BIRTH,
        default=BIRTH[0][0],
    )
    died = models.CharField(
        max_length=1,
        choices=DEATH,
        default=DEATH[0][0],
    )
    wikilink = models.URLField(max_length=200)
    image = models.ImageField(upload_to='images/')
    note = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'elephant_id': self.id })
 
class Care(models.Model):
    date = models.DateField('care date')
    care = models.CharField(
        max_length=1,
        choices=CARE,
        default=CARE[0][0],
        )
    elephant = models.ForeignKey(Elephant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_care_display()} on {self.date}"