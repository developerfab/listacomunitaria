from django.views.generic.edit import CreateView
from django.http import HttpResponse
from forms import UserForm
from django.shortcuts import render
from generador.models import Lista
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User


def Home(request):
    diccionario={'estado1':'active'}
    return render(request,'index.html',diccionario)

class Registro(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registro.html'
    success_url = reverse_lazy('inicio')

def Ingreso(request):
    model = User
    form_class = IngresoForm
    template_name = 'ingreso.html'
    success_url = reverse_lazy('logeo')
