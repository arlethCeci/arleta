from django.db import models
from django import forms

class UsuUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    strNombre = models.CharField(max_length=20)
    strPassword = models.CharField(max_length=20)
    idUsuCatEstado = models.IntegerField()
    idUsuCatTipoUsuario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'UsuUsuario'

class UsuCatEstado(models.Model):
    id = models.AutoField(primary_key=True)
    strNombreEstado = models.CharField(max_length=20)
    strDescripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'UsuCatEstado'

class UsuCatTipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    strTipoUsuario = models.CharField(max_length=50)
    strDescripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'UsuCatTipoUsuario'

        
class Producto(models.Model):
    idPro = models.AutoField(primary_key=True)
    StrNombrePro = models.CharField(max_length=100)
    StrDescriptcion = models.CharField(max_length=255)
    idProCatCategoria = models.ForeignKey('ProCatCategoria', on_delete=models.CASCADE, db_column='idProCatCategoria')
    idProCatSubCategoria = models.ForeignKey('ProCatSubCategoria', on_delete=models.CASCADE, db_column='idProCatSubCategoria') 
    decMaximo = models.DecimalField(max_digits=10, decimal_places=2)
    decMinimo = models.DecimalField(max_digits=10, decimal_places=2)
    curCosto = models.DecimalField(max_digits=10, decimal_places=2)
    curPrecio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    blodImage = models.ImageField(upload_to='productos/', null=True, blank=True)
    strUrlImage = models.CharField(max_length=255, null=True, default='')  

    class Meta:
        managed = False
        db_table = 'proproducto'

class ProCatSubCategoria(models.Model):
    idSubCat = models.AutoField(primary_key=True)
    strNombreSubCategoria = models.CharField(max_length=100)
    strDescripcionSubCategoria = models.CharField(max_length=255)
    idProCatCategoria = models.ForeignKey('ProCatCategoria', on_delete=models.CASCADE, db_column='idProCatCategoria')

    class Meta:
        managed = False
        db_table = 'procatsubcategoria'
        

class ProCatCategoria(models.Model):
    idCat = models.AutoField(primary_key=True)
    strNombreCategoria = models.CharField(max_length=100)
    strDescripcionCategoria = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'procatcategoria'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'  # Esto incluirá todos los campos del modelo

    # Agregar el campo de imagen al formulario
    blodImage = forms.ImageField()


class VenVentaCategoria(models.Model):
    idVenCat = models.AutoField(primary_key=True)
    strNombreVentaCategoria = models.CharField(max_length=20)
    srtDescripcionVentaCategoria = models.CharField(max_length=20, null=True)

    class Meta:
        managed = False
        db_table = 'venventacategoria'

class VenVenta(models.Model):
    idVenta = models.AutoField(primary_key=True)
    idUsuUsuario = models.ForeignKey(UsuUsuario, on_delete=models.CASCADE, db_column='idUsuUsuario')
    strFolio = models.CharField(max_length=30, null=True)
    dtFecha = models.DateField(null=True)
    idVenCatEstado = models.ForeignKey(VenVentaCategoria, on_delete=models.CASCADE, db_column='idVenCatEstado')

    class Meta:
        managed = False
        db_table = 'venventa'

class VenVentaProducto(models.Model):
    idVenPro = models.AutoField(primary_key=True)
    idVenVenta = models.IntegerField()
    idProProducto = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para el precio del producto
    decCantidad = models.DecimalField(max_digits=10, decimal_places=0)
    curTotal = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False  # Indica que Django no gestionará la tabla (ya que ya existe)
        db_table = 'venventaproducto'