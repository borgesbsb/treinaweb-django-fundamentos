from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Cliente
from .forms import ClienteForm, EnderecoForm
from .entidades import cliente
from .services import cliente_service

# Create your views here.

def listar_clientes(request):
    clientes = cliente_service.listar_clientes()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

# @csrf_exempt
# Desativando a proteção CSRF
def inserir_cliente(request):
    if request.method == "POST":
        form_cliente = ClienteForm_clienteform_cliente(request.POST)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data["nome"]
            sexo = form_cliente.cleaned_data["sexo"]
            data_nascimento = form_cliente.cleaned_data["data_nascimento"]
            email = form_cliente.cleaned_data["email"]
            profissao = form_cliente.cleaned_data["profissao"]
            cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, data_nascimento=data_nascimento, email=email,
                                           profissao=profissao)
            cliente_service.cadastrar_cliente(cliente_novo)
            return redirect('listar_clientes')
    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoForm()
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco })

def listar_cliente_id(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    return render(request, 'clientes/lista_cliente.html', {'cliente': cliente})

def editar_cliente(request, id):
    cliente_antigo = cliente_service.listar_cliente_id(id)
    form = ClienteForm(request.POST or None, instance=cliente_antigo)
    if form.is_valid():
        nome = form.cleaned_data["nome"]
        sexo = form.cleaned_data["sexo"]
        data_nascimento = form.cleaned_data["data_nascimento"]
        email = form.cleaned_data["email"]
        profissao = form.cleaned_data["profissao"]
        cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, data_nascimento=data_nascimento, email=email,
                                       profissao=profissao)
        cliente_service.editar_cliente(cliente_antigo, cliente_novo)
        return redirect('listar_clientes')
    return render(request, 'clientes/form_cliente.html', {'form': form})

def remover_cliente(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    if request.method == "POST":
        cliente_service.remover_cliente(cliente)
        return redirect('listar_clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente': cliente})
