from django.shortcuts import render
from django.http import HttpResponse
from .models import Paciente
from .forms import PacienteForm
from .tasks import *

from django_q.tasks import async_task
from django.contrib import messages

def cadastro_vacina(request):
    async_task("covidlocal.tasks.sincronizar")
    return render(request, "cadastro_vacina.html", {})

def cadastro_paciente(request):
    form = PacienteForm()
    if request.method == "POST":
        try:
            form = PacienteForm(request.POST)
            if form.is_valid():
                Paciente.objects.create(**form.cleaned_data)
                messages.success(request, 'Cadastro criado com sucesso!')
        except:
            messages.error(request,'Paciente já cadastrado!')
            pass
    context = {
        'form': form
    }
    return render(request, "cadastro_paciente.html", context)

def menu_inicial(request):
    return render(request, "menu_inicial.html", {})