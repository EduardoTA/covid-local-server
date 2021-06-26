from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Paciente
from .forms import PacienteForm
from .tasks import *

from django_q.tasks import async_task
from django.contrib import messages

@login_required
def cadastro_vacina(request):
    async_task("covidlocal.tasks.sincronizar")
    return render(request, "cadastro_vacina.html", {})

@login_required
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

@user_passes_test(lambda u: u.is_superuser)
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request, 'cadastrar_usuario.html', {'form': form})

@login_required
def cadastro_vacina(request):
    if request.method == 'POST':
        q = request.POST.get('q')
        paciente = Paciente.objects.filter(CPF__iexact=q).values()
        form = PacienteForm('dados')
        return render(request, 'cadastro_vacina.html', {'q':q,'paciente':paciente, 'form':form})
    return render(request, "cadastro_vacina.html", {})