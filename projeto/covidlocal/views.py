#from projeto.covidlocal.forms import PacienteForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Paciente
from .forms import PacienteForm

def cadastro_vacina(request):
    return HttpResponse("<h1>hello world!</h1>")

def cadastro_paciente(request):
    form = PacienteForm(request.POST or None)

    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "cadastro_paciente.html", context)

def menu_inicial(request):
    return render(request, "menu_inicial.html", {})