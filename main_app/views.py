from django.shortcuts import render
from django.http import HttpResponse
from .models import Elephant
import requests


# class Elephant:
#     def __init__(self, name, affiliation, species, sex, fictional, dob, dod, wikilink, image, note):
#         self.name = name
#         self.affiliation = affiliation
#         self.species = species
#         self.sex = sex
#         self.fictional = fictional
#         self.dob = dob
#         self.dod = dod
#         self.wikilink = wikilink
#         self.image = image
#         self.note = note

# elephants = [
#     Elephant('Abul-Abbas', 'Charlemagne', 'Asian', 'Male', 'false', 'Unavailable', '810', 'https://en.wikipedia.org/wiki/Abul-Abbas', 'https://elephant-api.herokuapp.com/pictures/001.jpg', 'An elephant given to Carolingian emperor Charlemagne by the Abbasid caliph Harun al-Rashid.')
#     # Elephant('Balarama', 'Dasara', 'Asian', 'Male', 'false', '1958', ' - ', 'https://en.wikipedia.org/wiki/Balarama_(elephant)', 'https://elephant-api.herokuapp.com/pictures/missing.jpg', 'A lead elephant of the world-famous Mysore Dasara procession.')
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def elephants_index(request):
    response = requests.get('https://elephant-api.herokuapp.com/elephants')
    elephants = response.json()
    return render(request, 'elephants/index.html', { 'elephants': elephants })