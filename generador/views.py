from django.views.generic.edit import CreateView
from django.http import HttpResponse
from forms import UserForm
from django.shortcuts import render

def Home(request):
    diccionario={'estado1':'active'}
    return render(request,'index.html',diccionario)
