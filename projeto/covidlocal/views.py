from django.shortcuts import render
from django.http import HttpResponse
from .models import Paciente
#from .forms import PacienteForm

# Create your views here.

    # path('admin/', admin.site.urls),
    # path('cadastro_paciente/', views.cadastro_paciente, name = 'paciente'),
    # path('cadastro_vacina/', views.cadastro_vacina, name = 'vacina'),
    # path('login/', views.login, name = 'login')

def cadastro_paciente(request):
    return HttpResponse("<h1>hello world!</h1>")

def cadastro_vacina(request):
    # form = VacinaForm(request.POST or None)

    # if form.is_valid():
    #     form.save()
    # context{
    #     'form': form
    #}
    return render(request, "cadastro_vacina.html", {})

def menu_inicial(request):
    return render(request, "menu_inicial.html", {})