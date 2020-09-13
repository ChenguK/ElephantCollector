from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage

from .models import Elephant, Care
from .forms import CareForm
# import requests




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
    care_form = CareForm()
    return render(request, 'elephants/detail.html', { 
        'elephant': elephant,
        'care_form': care_form,
         })

def add_care(request, elephant_id):
    form = CareForm(request.POST)
    if form.is_valid():
        new_care = form.save(commit=False)
        new_care.elephant_id = elephant_id
        new_care.save()
    return redirect('detail', elephant_id=elephant_id)

class ElephantCreate(CreateView):
    model = Elephant
    fields = '__all__'

class ElephantUpdate(UpdateView):
    model = Elephant
    fields = ['affiliation', 'species', 'sex', 'birthdate', 'died', 'wikilink', 'image', 'note']

class ElephantDelete(DeleteView):
    model = Elephant
    success_url = '/elephants/'
