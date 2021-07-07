from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Paciente
from .forms import PacienteForm
from .tasks import *
from django import forms

from django_q.tasks import async_task
from django.contrib import messages

@user_passes_test(lambda u: u.is_superuser)
def sincronizar(request):
    if request.method == "GET":
        async_task("covidlocal.tasks.sincronizar")
        return HttpResponse(status=201)

@login_required
def cadastro_paciente(request):
    paciente = 0
    form = PacienteForm()
    if request.method == "POST":
        try:
            form = PacienteForm(request.POST)
            if form.is_valid():
                paciente = Paciente.objects.create(**form.cleaned_data)
                messages.success(request, 'Cadastro criado com sucesso!')
        except:
            messages.error(request,'Paciente já cadastrado!')
            pass
    context = {
        'form': form,
        'paciente': paciente
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
    confirmado = 0
    if request.method == 'POST':
        if request.POST.get('confirma_cadastro'):
            try:
                form = PacienteForm(request.POST)
                if form.is_valid():
                    form_dict = form.cleaned_data
                    pk = ''
                    if form_dict.get('CPF') != '':
                        pk = form_dict.get('CPF')
                    else:
                        pk = form_dict.get('CNS')
                    Paciente.objects.filter(CPF=pk).update(**form_dict)
                    paciente = Paciente.objects.filter(CPF=pk).values()[0]
                    messages.success(request, 'Dados confirmados com sucesso!')
                    confirmado = 1
            except:
                messages.error(request,'Erro!')
                pass
            return render(request, 'cadastro_vacina.html', {'form':form, 'paciente': paciente, 'confirmado': confirmado})
        else:
            pesquisa = request.POST.get('pesquisa')
            try:
                paciente = 0
                if Paciente.objects.filter(CPF__iexact=pesquisa):
                    paciente = Paciente.objects.filter(CPF__iexact=pesquisa).values()[0]
                    paciente.pop('id')
                elif Paciente.objects.filter(CNS__iexact=pesquisa):
                    paciente = Paciente.objects.filter(CNS__iexact=pesquisa).values()[0]
                    paciente.pop('id')
                else:
                    messages.error(request,'Paciente ainda não está cadastrado!')
                form = PacienteForm(paciente)
            except:
                messages.error(request,'Erro!')
                pass
            return render(request, 'cadastro_vacina.html', {'pesquisa':pesquisa,'paciente':paciente, 'form':form, 'confirmado': confirmado})
    return render(request, "cadastro_vacina.html", {'confirmado': confirmado})

@login_required
def cadastro_imunizacao(request):
    return render(request, "cadastro_imunizacao.html", {})
