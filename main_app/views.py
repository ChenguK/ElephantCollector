from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
from .models import Elephant
import requests


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def elephants_index(request):
    elephants = Elephant.objects.all()
    return render(request, 'elephants/index.html', { 'elephants': elephants })

def elephants_detail(request, elephant_id):
    elephant = Elephant.objects.get(id=elephant_id)
    return render(request, 'elephants/detail.html', { 'elephant': elephant })

class ElephantCreate(CreateView):
    model = Elephant
    fields = '__all__'

class ElephantUpdate(UpdateView):
    model = Elephant
    fields = ['affiliation', 'species', 'sex', 'fictional', 'dob', 'dod', 'wikilink', 'image', 'note']

class ElephantDelete(DeleteView):
    model = Elephant
    success_url = '/elephants/'
