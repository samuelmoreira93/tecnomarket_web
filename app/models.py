from django.db import models

class Marca(models.Model):
    nombre=models.CharField(max_length=50)

    class Meta:
        verbose_name ='Marca'
        verbose_name_plural ='Marcas'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    marca=models.ForeignKey(Marca,on_delete=models.PROTECT) #envia una adventencia antes de eliminar
    fecha_fabricacion=models.DateField()
    imagen=models.ImageField(upload_to='productos',null=True, blank=True)

    class Meta:
        verbose_name ='Producto'
        verbose_name_plural ='Productos'

    def __str__(self):
        return self.nombre

opciones_consultas=[
    [0, "consulta"],
    [1,"reclamos"],
    [2, "sugerencias"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    tipo_consulta=models.IntegerField(choices=opciones_consultas)
    mensaje=models.TextField()
    avisos=models.BooleanField()

    def __str__(self):
        return self.nombre