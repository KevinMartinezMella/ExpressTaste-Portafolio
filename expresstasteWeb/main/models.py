from django.db import models

class Rol(models.Model):
    rol = models.CharField(max_length=90)

class Usuario(models.Model):
    nombre          = models.CharField(max_length=50)
    ap_paterno      = models.CharField(max_length=50)
    ap_materno      = models.CharField(max_length=50)
    email           = models.CharField(max_length=90)
    contrasena      = models.CharField(max_length=70)
    rol             = models.ForeignKey(Rol, on_delete=models.PROTECT)
    fecha_creacion  = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.nombre}'

class TipoNegocio(models.Model):
    tipo = models.CharField(max_length=90)

class Negocio(models.Model):
    negocio         = models.CharField(max_length=90)
    descripcion     = models.CharField(max_length=500)
    tipo_negocio    = models.ForeignKey(TipoNegocio, on_delete=models.PROTECT)
    usuario         = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion  = models.DateTimeField(auto_now_add=True)

class Categoria(models.Model):
    categoria       = models.CharField(max_length=50)
    imagen          = models.ImageField(upload_to='categorias')
    negocio         = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    fecha_creacion  = models.DateTimeField(auto_now_add=True)

class Producto(models.Model):
    producto        = models.CharField(max_length=50)
    imagen          = models.ImageField(upload_to='productos')
    precio          = models.IntegerField(default=0)
    categoria       = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    detalle         = models.CharField(max_length=500)
    fecha_creacion  = models.DateTimeField(auto_now_add=True)

class Mesa(models.Model):
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    mesa    = models.CharField(max_length=50)

class EstadoPedido(models.Model):
    estado = models.CharField(max_length=50)

class Pedido(models.Model):
    usuario         = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    precio_total    = models.IntegerField()
    mesa            = models.ForeignKey(Mesa, on_delete=models.PROTECT)
    estado          = models.ForeignKey(EstadoPedido, on_delete=models.PROTECT)
    fecha_creacion  = models.DateTimeField(auto_now_add=True)

class DetallePedido(models.Model):
    producto        = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad        = models.IntegerField()
    precio_unitario = models.IntegerField()
    precio_final    = models.IntegerField()
    pedido          = models.ForeignKey(Pedido, on_delete=models.CASCADE)