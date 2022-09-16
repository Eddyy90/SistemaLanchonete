from django.shortcuts import render
from .forms import *

def cadastrar_usuario(request):

    form = CadForm()

    if request.method == 'POST':
        form = CadForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            salvando = CadForm(nome=nome, email=email, senha=senha)
            salvando.save()

    return render(request, "cad_form.html", {'cad_form':form})

def login_usuario(request):

    form = LoginForm()

    if request.method == 'GET':
        form = LoginForm(request.GET)

        if form.is_valid():
            email = form.changed_data['email']
            senha = form.changed_data['senha']

            autenticando = LogUser(email=email, senha=senha)
            autenticando.check()    
    