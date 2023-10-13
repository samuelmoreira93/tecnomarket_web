from django.shortcuts import render,redirect,get_object_or_404
from .models import Producto
from .forms import ContactoForm,ProductoForm,CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate,login
from rest_framework import viewsets
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


def home(request):
    productos=Producto.objects.all()

    context={
        'productos': productos
    }

    return render(request,'app/home.html',context)


def contacto(request):
    context={
        'forms': ContactoForm
    }
    if request.method == 'POST':
        formulario=ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            context['mensaje']= 'contacto guardado'
        else:
            context['forms'] = formulario

    return render(request,'app/contacto.html',context)


def galeria(request):
    return render(request,'app/galeria.html')


def agregar_producto(request):

    context={
        'forms': ProductoForm
    }

    if request.method == 'POST':
        formulario=ProductoForm(data=request.POST,files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto registrado')
        else:
            context['forms']=formulario
        
        return redirect(to='listar-producto')


    return render(request,'app/producto/agregar.html',context)


def listar_productos(request):
    productos=Producto.objects.all()
    page=request.GET.get('page',1)

    try:
        paginator=Paginator(productos,4)
        productos=paginator.page(page)
    except:
        raise Http404
    
    context={
        'entity': productos,
        'paginator':paginator
    }
    
    return render(request,'app/producto/listar.html',context)



def modificar_producto(request,id):

    producto=get_object_or_404(Producto,id=id)

    context={
        'forms':ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario=ProductoForm(data=request.POST,instance=producto,files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado Correctamente")

            return redirect(to='listar-producto')
        else:
            context['forms']=formulario


    return render(request,'app/producto/modificar.html',context)



def eliminar_producto(request,id):

    producto=get_object_or_404(Producto,id=id)
    producto.delete()
    messages.success(request,"Eliminado Correctamente")
    return redirect(to='listar-producto')



def registro(request):
    context={
        'form':CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request,user)
            messages.success(request, 'Te has registrado correctamente')
            return redirect(to='home')
        context['form']=formulario

    return render(request,'registration/registro.html',context)