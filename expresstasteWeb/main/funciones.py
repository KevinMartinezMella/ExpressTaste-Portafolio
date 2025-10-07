from django.http import HttpResponse
from . models import Negocio

def validar_negocio(id_usuario):
    cantidad_negocios = Negocio.objects.filter(usuario_id = id_usuario).count()
    return cantidad_negocios