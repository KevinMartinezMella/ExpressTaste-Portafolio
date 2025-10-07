from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from . models import Usuario, Categoria, Producto, TipoNegocio, Negocio, EstadoPedido, Mesa, Pedido, DetallePedido, Rol
from . serializers import UsuarioSerializer, CategoriaSerializer, ProductoSerializer, NegocioSerializer, TipoNegocioSerializer, MesaSerializer, EstadoPedidoSerializer, PedidoSerializer, DetallePedidoSerializer, RolSerializer

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import funciones


def principal(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST["correo"]
        contrasena = request.POST["contrasena"]
        
        usuario = Usuario.objects.filter(['email', email], ['contrasena', contrasena])

        if(len(usuario) > 0):
            request.session["id_usuario"] = usuario[0].id
            request.session["nombre_usuario"] = f'{usuario[0].nombre} {usuario[0].ap_paterno}'

            cantidad_negocios = funciones.validar_negocio(usuario[0].id)

            if(cantidad_negocios == 0):
                return redirect('registro_negocio')

            return redirect('seleccion')

    return render(request, 'autenticacion/login.html')

def registro(request):
    if(request.method == 'POST'):
        nombre      = request.POST["nombre"]
        ape_paterno = request.POST["ape_paterno"]
        ape_materno = request.POST["ape_materno"]
        email       = request.POST["correo"]
        contrasena  = request.POST["contrasena"]
        contar = Usuario.objects.filter(email = email)
        if(len(contar) > 0):
            errores = {
                'mensaje': 'Este correo electrónico ya se encuentra registrado.',
                'nombre': nombre,
                'ape_paterno': ape_paterno,
                'ape_materno': ape_materno,
                'email': email
            }
            return render(request, 'autenticacion/registro.html', errores)
        rol = Rol.objects.get(['id', 1])
        usuario = Usuario(
            nombre      = nombre,
            ap_paterno  = ape_paterno,
            ap_materno  = ape_materno,
            email       = email,
            contrasena  = contrasena,
            rol         = rol
        )
        usuario.save()

        request.session["id_usuario"] = usuario.id
        request.session["nombre_usuario"] = f'{usuario.nombre} {usuario.ap_paterno}'

        msg_html = render_to_string('correos/registro.html', {'nombre': nombre.capitalize()})
        email_message = EmailMessage(
            subject="ExpressTaste - Registro Exitoso 🎉",
            body=msg_html,
            from_email="ExpressTaste <envio6697@gmail.com>",
            to=[email],
        )
        email_message.content_subtype = "html"
        email_message.send(fail_silently=False)

        cantidad_negocios = funciones.validar_negocio(usuario.id)

        if(cantidad_negocios == 0):
            return redirect('registro_negocio')
        

        return redirect('panel')
    return render(request, 'autenticacion/registro.html')

def categorias(request):
    if 'id_usuario' in request.session:
        negocio = Negocio.objects.get(id = request.session["id_negocio"])
        categorias = Categoria.objects.filter(negocio = negocio.id)
        return render(request, 'administrador/categorias.html', {'categorias': categorias})
    return redirect('login')

def productos(request):
    if 'id_usuario' in request.session:
        negocio = Negocio.objects.get(id = request.session["id_negocio"])
        categorias = Categoria.objects.filter(negocio = negocio.id)
        productos = Producto.objects.filter(categoria__in=categorias)
        datos = {
            'productos': productos,
            'categorias': categorias,
        }
        return render(request, 'administrador/productos.html', datos)
    return redirect('login')

def mesas(request):
    if 'id_usuario' in request.session:
        negocio = Negocio.objects.get(id = request.session["id_negocio"])
        mesas = Mesa.objects.filter(negocio = negocio)
        return render(request, 'administrador/mesas.html', {'mesas': mesas})
    return redirect('login')

def usuarios(request):
    if 'id_usuario' in request.session:
        return render(request, 'administrador/usuarios.html')
    return redirect('login')

def seleccion(request):
    if 'id_usuario' in request.session:
        usuario = Usuario.objects.get(id = request.session["id_usuario"])
        negocios = Negocio.objects.filter(usuario = usuario)
        if request.method == 'POST':
            request.session["id_negocio"] = request.POST["id_negocio"]
            return redirect('panel')
        return render(request, 'administrador/seleccion.html', {'negocios' : negocios})
    return redirect('login')

def registro_negocio(request):
    if 'id_usuario' in request.session:
        tipo_negocios = TipoNegocio.objects.all()
        print(tipo_negocios)
        return render(request, 'administrador/negocio.html', {'tipo_negocios': tipo_negocios})
    return redirect('login')

def panel(request):
    if 'id_usuario' in request.session:
        return render(request, 'administrador/panel.html')
    return redirect('login')


# API
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer

class TipoNegocioViewSet(viewsets.ModelViewSet):
    queryset = TipoNegocio.objects.all()
    serializer_class = TipoNegocioSerializer

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class EstadoPedidoViewSet(viewsets.ModelViewSet):
    queryset = EstadoPedido.objects.all()
    serializer_class = EstadoPedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer