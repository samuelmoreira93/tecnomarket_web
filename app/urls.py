from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto',views.ProductoViewSet)

urlpatterns = [
    path('',views.home,name='home'),
    path('contacto/',views.contacto,name='contacto'),
    path('galeria/',views.galeria,name='galeria'),
    path('agregar-producto/',views.agregar_producto,name='agregar-producto'),
    path('listar-producto/',views.listar_productos,name='listar-producto'),
    path('modificar-producto/<id>/',views.modificar_producto,name='modificar-producto'),
    path('eliminar-producto/<id>/',views.eliminar_producto,name='eliminar-producto'),
    path('registro/',views.registro,name='registro'),
    path('api/',include(router.urls)),
]
