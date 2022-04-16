from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Widgets

# Define the home view

class AddWidgets(CreateView):
    widgets = Widgets.objects.all()
    model = Widgets
    fields = '__all__'
    sussess_url = '/'

def index(request):
  return render(request, 'index.html')

class DeleteWidget(DeleteView):
  model = Widgets
  success_url = '/'