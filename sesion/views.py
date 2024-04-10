from django.shortcuts import render, redirect
from .models import UsuUsuario
from .forms import UsuarioForm
from .models import UsuCatTipoUsuario
from .models import UsuCatEstado
from .models import Producto, ProCatCategoria, ProCatSubCategoria
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import ProductoForm
from .models import VenVenta
from datetime import datetime
from django.http import JsonResponse
from .models import VenVentaProducto





from django.shortcuts import render, redirect
from .models import UsuUsuario
from .forms import UsuarioForm
from .models import UsuCatTipoUsuario
from .models import UsuCatEstado
from .models import VenVentaCategoria

 

def sesion(request):
    if request.method == 'POST':
        nombre_usuario = request.POST['nombre_usuario']
        contraseña = request.POST['contraseña']
   
        try:
            usuario = UsuUsuario.objects.get(strNombre=nombre_usuario, strPassword=contraseña)
        except UsuUsuario.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'Usuario o contraseña incorrectos'})
        
        return redirect('principal') 
        
    return render(request, 'login.html')


def bienvenida(request):
    return render(request, 'bienvenida.html')
    
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UsuCatTipoUsuario, UsuCatEstado
from .forms import UsuarioForm  

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)  
        if form.is_valid(): 
            form.save()  
            messages.success(request, 'Usuario agregado exitosamente.')
            return redirect('bienvenida')
        else:
            messages.error(request, 'Error en el formulario. Por favor, corrige los errores e intenta de nuevo.')
            return redirect('bienvenida')
    else:
        tipos_usuario = UsuCatTipoUsuario.objects.all()
        estados = UsuCatEstado.objects.all()
        form = UsuarioForm() 
        return render(request, 'agregar_usuario.html', {
            'form': form,
            'tipos_usuario': tipos_usuario,
            'estados': estados,
        })
    
   
from django.core.paginator import Paginator

def bienvenida(request):
    lista_usuarios =  UsuUsuario.objects.all()  
    paginator = Paginator(lista_usuarios, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'bienvenida.html', {'page_obj': page_obj})



from django.shortcuts import render, redirect, get_object_or_404
from .models import UsuUsuario, VenVenta, VenVentaProducto

def eliminar_usuario(request, usuario_id):
   
    usuario = get_object_or_404( UsuUsuario,id=usuario_id)
    
    if request.method == 'POST':
       
        usuario.delete()
  
        return redirect('bienvenida') 

    return render(request, 'eliminar_usuario.html', {'usuario': usuario})

from django.shortcuts import render, redirect


def editar_usuario(request, usuario_id):
    usuario = UsuUsuario.objects.get(id=usuario_id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        estado = request.POST.get('estado')
        tipo_usuario = request.POST.get('tipo_usuario')
        
     
        usuario.strNombre = nombre
        usuario.idUsuCatEstado = estado
        usuario.idUsuCatTipoUsuario = tipo_usuario
        usuario.save()

       
        return redirect('bienvenida')

    return render(request, 'EditarUsuario.html', {'usuario': usuario})

def buscar_usuarios(request):
    nombre = request.GET.get('nombre')
    estado = request.GET.get('estado')
    tipo = request.GET.get('tipo')

    usuarios =UsuUsuario.objects.all()

    if nombre:
        usuarios = usuarios.filter(strNombre__icontains=nombre)
    if estado:
        usuarios = usuarios.filter(idUsuCatEstado=estado)
    if tipo:
        usuarios = usuarios.filter(idUsuCatTipoUsuario=tipo)

    return render(request, 'tu_template.html', {'usuarios': usuarios})





from django.core.paginator import Paginator

def producto(request):
    categorias = ProCatCategoria.objects.all()
    subcategorias = ProCatSubCategoria.objects.all()
    productos = Producto.objects.all()

    # Definir la cantidad de productos por página
    productos_por_pagina = 4

    if request.method == 'POST':
        categoria_id = request.POST.get('categoria')
        subcategoria_id = request.POST.get('subcategoria')
        nombre_producto = request.POST.get('nombre_producto')  

        if categoria_id:
            productos = Producto.objects.filter(idProCatCategoria=categoria_id)
        elif subcategoria_id:
            productos = Producto.objects.filter(idProCatSubCategoria=subcategoria_id)
        
        if nombre_producto:
            productos = productos.filter(StrNombrePro__icontains=nombre_producto)
    
    # Inicializar el paginador
    paginator = Paginator(productos, productos_por_pagina)
    
    # Obtener el número de página
    page_number = request.GET.get('page')
    
    # Obtener los objetos de la página actual
    page_obj = paginator.get_page(page_number)

    return render(request, 'producto.html', {'categorias': categorias, 'subcategorias': subcategorias, 'productos': page_obj})

def agregar_producto(request):
    categorias = ProCatCategoria.objects.all()
    subcategorias = ProCatSubCategoria.objects.all()

    if request.method == 'POST':
       
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        tipo_producto_id = request.POST.get('tipo_producto')  
        subtipo_producto_id = request.POST.get('subtipo_producto')  
        maximo = request.POST.get('maximo')
        minimo = request.POST.get('minimo')
        costo = request.POST.get('costo')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        
     
        tipo_producto = ProCatCategoria.objects.get(idCat=tipo_producto_id)
        subtipo_producto = ProCatSubCategoria.objects.get(idSubCat=subtipo_producto_id)
        
     
        producto = Producto(
            StrNombrePro=nombre,
            StrDescriptcion=descripcion,
            idProCatCategoria=tipo_producto,
            idProCatSubCategoria=subtipo_producto,
            decMaximo=maximo,
            decMinimo=minimo,
            curCosto=costo,
            curPrecio=precio,
            stock=stock
        )
        
  
        producto.save()

    
        return redirect('producto')

    else:
        # Renderizar el formulario de agregar producto
        return render(request, 'agregar_producto.html', {'categorias': categorias, 'subcategorias': subcategorias})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, VenVentaProducto

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, idPro=producto_id)
    
    if request.method == 'POST':
        # Eliminar registros relacionados en VenVentaProducto
        VenVentaProducto.objects.filter(idProProducto=producto_id).delete()
        
        # Eliminar el producto
        producto.delete()
        
        # Redirigir a la página de productos
        return redirect('producto')
    
    return render(request, 'eliminar_producto.html', {'producto': producto})


from django.shortcuts import render, redirect
from .forms import ProductoForm  # Importa tu formulario

def editar_producto(request, producto_id):
    producto = Producto.objects.get(idPro=producto_id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto) 
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'editar_producto.html', {'form': form, 'producto_id': producto_id})

def puntoventa(request):
    return render(request, 'Puntoventa.html') 



from .models import ProCatCategoria, ProCatSubCategoria
from .models import Producto


from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from django.core import serializers

def agregar_venta(request):
    if request.method == 'POST':
        folio_seleccionado = request.POST.get('folio')

        # Obtener el ID de la venta asociada al folio seleccionado
        venta = VenVenta.objects.filter(strFolio=folio_seleccionado).first()
        if not venta:
            return HttpResponse('No se encontró ninguna venta asociada al folio seleccionado.')

        id_ven_venta = venta.idVenta
        
        # Obtener los productos agregados al carrito
        productos_carrito = request.session.get('productos_carrito', [])

        # Guardar cada producto del carrito en la tabla VenVentaProducto
        for producto in productos_carrito:
            id_pro_producto = producto['id']
            dec_cantidad = producto['cantidad']
            cur_total = producto['total']

            venta_producto = VenVentaProducto(
                idVenVenta=id_ven_venta,
                idProProducto=id_pro_producto,
                decCantidad=dec_cantidad,
                curTotal=cur_total
            )
            venta_producto.save()

        return redirect('puntoventa')

    folios = VenVenta.objects.values_list('strFolio', flat=True).distinct()
    categorias = ProCatCategoria.objects.all()
    subcategorias = ProCatSubCategoria.objects.all()
    productos = []

    context = {'folios': folios, 'categorias': categorias, 'subcategorias': subcategorias, 'productos': productos}
    return render(request, 'agregar_venta.html', context)

def almacenar_carrito(request):
    if request.method == 'POST':

        id_ven_venta = request.POST.get('idVenVenta')
        if not id_ven_venta:
            return JsonResponse({'error': 'No se ha proporcionado el ID de la venta'}, status=400)

        data = json.loads(request.body)
        
        if not data:
            return JsonResponse({'error': 'No se han proporcionado datos JSON'}, status=400)
        
        productos_carrito = data.get('productos_carrito')

        for producto in productos_carrito:
            id_pro_producto = producto['producto']
            dec_cantidad = producto['cantidad']
            cur_total = producto['total']


            venta_producto = VenVentaProducto(
                idVenVenta=id_ven_venta, 
                idProProducto=id_pro_producto,
                decCantidad=dec_cantidad,
                curTotal=cur_total
            )

        
            venta_producto.save()

        return JsonResponse({'message': 'Datos del carrito almacenados exitosamente'})
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)

def get_productos(request):
    categoria_id = request.GET.get('categoria_id')
    subcategoria_id = request.GET.get('subcategoria_id')
    
    print("categoria_id:", categoria_id)
    print("subcategoria_id:", subcategoria_id)

    productos = []
    if categoria_id and subcategoria_id:
        productos = Producto.objects.filter(idProCatCategoria=categoria_id, idProCatSubCategoria=subcategoria_id).values('idPro', 'StrNombrePro')
    
    return JsonResponse(list(productos), safe=False)

def get_producto_details(request):
    if request.method == 'GET':
        producto_id = request.GET.get('producto_id')
        producto = Producto.objects.get(idPro=producto_id)
        data = {
            'stock': producto.stock,
            'precio': producto.curPrecio,
        }
        return JsonResponse(data)

from .models import UsuUsuario, VenVenta, VenVentaCategoria



def registrar_venta(request):
    if request.method == 'POST':
      
        folio = request.POST.get('strFolio')
        usuario_id = request.POST.get('idUsuUsuario')
        fecha = request.POST.get('dtFecha')
        estado_venta_id = request.POST.get('idVenCatEstado')

        try:
            # Obtener la instancia de UsuUsuario a partir de su ID
            usuario = UsuUsuario.objects.get(id=usuario_id)
        except UsuUsuario.DoesNotExist:
            raise Http404("El usuario especificado no existe")

        try:
            # Obtener la instancia de VenVentaCategoria a partir de su ID
            categoria_venta = VenVentaCategoria.objects.get(idVenCat=estado_venta_id)
        except VenVentaCategoria.DoesNotExist:
            raise Http404("La categoría de venta especificada no existe")

        # Crear un objeto VenVenta y guardarlo en la base de datos
        venta = VenVenta(
            strFolio=folio,
            idUsuUsuario=usuario,
            dtFecha=datetime.strptime(fecha, '%Y-%m-%d'),
            idVenCatEstado=categoria_venta  # Utiliza idVenCatEstado en lugar de idVenCat
        )
        venta.save()

        # Redirigir a una página de éxito o a donde desees
        return redirect('puntoventa')

    else:
        # Si la solicitud es GET, renderizar el formulario
        usuarios = UsuUsuario.objects.all()
        categorias_venta = VenVentaCategoria.objects.all()
        return render(request, 'registrar_venta.html', {'usuarios': usuarios, 'categorias_venta': categorias_venta})


from django.shortcuts import render, redirect
from django.contrib.auth import logout

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        # Redirige a la página de sesión después de cerrar sesión
        return redirect('sesion')  # Ajusta 'sesion' a la URL de tu página de sesión
    else:
        return render(request, 'logout.html')


def principal(request):
    return render(request, 'Principal.html')