# forms.py
from django import forms
from .models import UsuUsuario
from .models import Producto 

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuUsuario
        fields = ['strNombre', 'strPassword', 'idUsuCatTipoUsuario', 'idUsuCatEstado']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['StrNombrePro', 'StrDescriptcion', 'idProCatCategoria', 'idProCatSubCategoria', 'decMaximo', 'decMinimo', 'curCosto', 'curPrecio', 'stock', 'blodImage']