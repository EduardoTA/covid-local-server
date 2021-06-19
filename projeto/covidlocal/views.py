#from projeto.covidlocal.forms import PacienteForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Paciente
from .forms import PacienteForm

def cadastro_vacina(request):
    return render(request, "cadastro_vacina.html", {})

def cadastro_paciente(request):
    form = PacienteForm()
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            Paciente.objects.create(**form.cleaned_data)
    context = {
        'form': form
    }
    return render(request, "cadastro_paciente.html", context)

def menu_inicial(request):
    return render(request, "menu_inicial.html", {})