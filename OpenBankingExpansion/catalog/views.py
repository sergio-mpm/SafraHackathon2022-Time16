from django.shortcuts import render
from django.db import connection
from catalog.models import *

# Create your views here.
def index(request):
    context ={}

    return render(request, 'Tela_1/index.html', context)


def Tela_2(request):
    context ={}

    return render(request, 'Tela_2/tela2.html', context)


def Tela_3(request):
    context ={}

    return render(request, 'Tela_3/tela3.html', context)


def Tela_4(request):
    context ={}

    if request.method == 'POST':
        CPF = request.POST.get('CPF')
        cliente = ValorCliente.objects.get(cpf=CPF)
        cliente.calcula_credito()
        proposta = PropostaCredito.objects.get(cliente.cliente_id)

    return render(request, 'Tela_4/tela4.html', context)


def Tela_5(request):
    context ={}

    return render(request, 'Tela_5/tela5.html', context)


def Tela_6(request):
    context ={}

    return render(request, 'Tela_6/tela6.html', context)
