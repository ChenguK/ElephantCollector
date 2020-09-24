from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.files.storage import FileSystemStorage

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os
import uuid
import boto3
from .models import Elephant, Trainer, Photo
from .forms import CareForm
# import requests

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector-ck'
# used a bucket from another project

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class ElephantList(LoginRequiredMixin, ListView):
    model = Elephant
    # paginate_by = 10

@login_required
def profile(request):
    elephants = Elephant.objects.filter(user=request.user)
    # paginate_by = 10
    return render(request, 'registration/user_index.html', { 'elephants': elephants })

@login_required
def elephants_detail(request, elephant_id):
    elephant = Elephant.objects.get(id=elephant_id)
    trainers_elephant_doesnt_have = Trainer.objects.exclude(id__in = elephant.trainers.all().values_list('id'))
    care_form = CareForm()
    return render(request, 'elephants/detail.html', { 
        'elephant': elephant,
        'care_form': care_form,
        'trainers': trainers_elephant_doesnt_have,
         })

@login_required
def add_care(request, elephant_id):
    form = CareForm(request.POST)
    if form.is_valid():
        new_care = form.save(commit=False)
        new_care.elephant_id = elephant_id
        new_care.save()
    return redirect('detail', elephant_id=elephant_id)

@login_required
def add_photo(request, elephant_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, elephant_id=elephant_id)
            photo.save()
        except:
            print('An error occurred uploading file to s3')
    return redirect('detail', elephant_id=elephant_id)

@login_required
def photos_delete(request, elephant_id, photo_id):
    context={}
    obj = get_object_or_404(Photo, id=photo_id)

    if request.method == 'GET':
        obj.delete()
        return redirect('detail', elephant_id)

@login_required
def assoc_trainer(request, elephant_id, trainer_id):
  Elephant.objects.get(id=elephant_id).trainers.add(trainer_id)
  return redirect('detail', elephant_id=elephant_id)

@login_required
def unassoc_trainer(request, elephant_id, trainer_id):
  Elephant.objects.get(id=elephant_id).trainers.remove(trainer_id)
  return redirect('detail', elephant_id=elephant_id)

class ElephantCreate(LoginRequiredMixin, CreateView):
    model = Elephant
    fields = ['name', 'affiliation', 'species', 'sex', 'birthdate', 'died', 'wikilink', 'note']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ElephantUpdate(LoginRequiredMixin, UpdateView):
    model = Elephant
    fields = ['affiliation', 'species', 'sex', 'birthdate', 'died', 'wikilink', 'note']

class ElephantDelete(LoginRequiredMixin, DeleteView):
    model = Elephant
    success_url = '/elephants/'

def trainers_index(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainers/index.html', { 'trainers': trainers })

def trainers_detail(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    return render(request, 'trainers/detail.html', { 'trainer': trainer})

class TrainerCreate(LoginRequiredMixin, CreateView):
    model = Trainer
    fields = '__all__'

class TrainerUpdate(LoginRequiredMixin, UpdateView):
    model = Trainer
    fields = ['color']

class TrainerDelete(LoginRequiredMixin, DeleteView):
    model = Trainer
    success_url = '/trainers/'