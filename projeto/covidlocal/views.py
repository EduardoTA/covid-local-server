from django.shortcuts import render
from django.http import HttpRensponse
from .models import Paciente

# Create your views here.

    # path('admin/', admin.site.urls),
    # path('cadastro_paciente/', views.cadastro_paciente, name = 'paciente'),
    # path('cadastro_vacina/', views.cadastro_vacina, name = 'vacina'),
    # path('login/', views.login, name = 'login')

def cadastro_paciente(request):
    return HttpRensponse("<h1>hello world!</h1>")