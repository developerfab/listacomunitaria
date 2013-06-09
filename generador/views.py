from django.views.generic.edit import CreateView
from django.http import HttpResponse
from forms import UserForm, IngresoForm
from django.shortcuts import render
from generador.models import Lista
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

"""
Pagina de inicio del sitio
"""
def Home(request):
    diccionario={'estado1':'active'}
    return render(request,'index.html',diccionario)

"""
Resgistro de un usuario
"""
class Registro(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registro.html'
    success_url = reverse_lazy('inicio')

"""
Formulario para hacer login al aplicativo
"""
class Ingreso(CreateView):
    model = User
    form_class = IngresoForm
    template_name = 'ingreso.html'
    success_url = reverse_lazy('logeo')

"""
Sitio para usuarios externos
"""
def Externo(request):
    diccionario={'estado3':'active'}
    return render(request,'externo.html',diccionario)

"""
Logeo del usuario
"""
def Logeo(request):
    usuario = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=usuario , password=password) 
    print (user)
    if user is not None:
        if user.is_active:
            print ('entra a usuario')
            Ventana_Usuario(request)
        else:
            diccionario = {}
            return render(request,'cuenta_desactivada.html',diccionario)
    else:
        diccionario = {}
        return render(request,'error_login',diccionario)

@login_required
def Ventana_Usuario(request):
    login(request,user)
    diccionario = {}
    return render(request,'interno.html',diccionario)
    
