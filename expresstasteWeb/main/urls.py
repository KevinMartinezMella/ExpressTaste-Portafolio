from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'usuarios',        views.UsuarioViewSet)
router.register(r'roles',           views.RolViewSet)
router.register(r'categorias',      views.CategoriaViewSet)
router.register(r'productos',       views.ProductoViewSet)
router.register(r'negocios',        views.NegocioViewSet)
router.register(r'tipos-negocio',   views.TipoNegocioViewSet)
router.register(r'mesas',           views.MesaViewSet)
router.register(r'estados-pedido',  views.EstadoPedidoViewSet)
router.register(r'pedidos',         views.PedidoViewSet)
router.register(r'detalle-pedido',  views.DetallePedidoViewSet)

urlpatterns = [
    path('',                    views.principal,            name="principal"),
    path('registro',            views.registro,             name="registro"),
    path('acceder',             views.login,                name="login"),
    path('panel',               views.panel,                name="panel"),
    path('categorias',          views.categorias,           name="categorias"),
    path('productos',           views.productos,            name="productos"),
    path('mesas',               views.mesas,                name="mesas"),
    path('usuarios',            views.usuarios,             name="usuarios"),
    path('seleccion',           views.seleccion,            name="seleccion"),
    path('registro-negocio',    views.registro_negocio,     name="registro_negocio"),

    # API
    path('api/v1/', include(router.urls))
]