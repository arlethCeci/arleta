<<<<<<< HEAD
"""
URL configuration for ventas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from sesion import views as sesion_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sesion/', sesion_views.sesion, name='sesion'),
    path('bienvenida/', sesion_views.bienvenida, name='bienvenida'),
    path('agregar_usuario/', sesion_views.agregar_usuario, name='agregar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', sesion_views.eliminar_usuario, name='eliminar_usuario'),
    path('editar_usuario/<int:usuario_id>/', sesion_views.editar_usuario, name='editar_usuario'),
    path('producto/', sesion_views.producto, name='producto'),
    path('agregar_producto/', sesion_views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:producto_id>/', sesion_views.eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:producto_id>/', sesion_views.editar_producto, name='editar_producto'),
    path('puntoventa/', sesion_views.puntoventa, name='puntoventa'),
    path('agregar_venta/', sesion_views.agregar_venta, name='agregar_venta'),
    path('registrar_venta',sesion_views.registrar_venta, name='registrar_venta'),
    path('get_productos/', sesion_views.get_productos, name='get_productos'),
    path('get_producto_details/', sesion_views.get_producto_details, name='get_producto_details'),
    path('logout/', sesion_views.logout_view, name='logout'),
    path('almacenar_carrito/', sesion_views.almacenar_carrito, name='almacenar_carrito'),
    path('principal/', sesion_views.principal, name='principal'),

]

# Configuración para servir archivos multimedia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
# En el archivo urls.py del proyecto principal
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/', include('ventas.urls')),  # Reemplaza 'tu_app' con el nombre de tu aplicación
]
>>>>>>> 398472b (Primer commit en la rama main)
