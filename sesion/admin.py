from django.contrib import admin
from .models import UsuUsuario, UsuCatEstado, UsuCatTipoUsuario
from .models import Producto

admin.site.register(UsuUsuario)
admin.site.register(UsuCatEstado)
admin.site.register(UsuCatTipoUsuario)
admin.site.register(Producto)

