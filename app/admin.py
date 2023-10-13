from django.contrib import admin
from .models import Marca,Producto,Contacto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio','nuevo','marca'] #Agregamos al admin las columnas que queremos ver
    list_editable = ['precio'] # Definimos que columas podemos modificar rapidamente desde el admin
    search_fields = ['nombre'] #Definimos una barra de busqueda con parametros
    list_filter = ['marca', 'nuevo'] #definimos un filtro por parametros
    list_per_page = 5  #Registra 5 productos por pagina desde el admin django

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)