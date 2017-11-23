from django.shortcuts import render, redirect
from perfis.models import Perfil


def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all()})

def exibir(request, perfil_id):
    #print('ID do perfil recebio: % s' % (perfil_id))
    perfil = Perfil.objects.get(id=perfil_id)

    return render(request, 'perfil.html', {"perfil": perfil})

def convidar(request, perfil_id):  # Funcion hereda parametros
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')  # Para redireccionar la funcion index y no repetir codigo


def get_perfil_logado(request):
    return Perfil.objects.get(id=1)