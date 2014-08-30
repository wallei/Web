from django.db import models
from datetime import datetime



class categoria(models.Model):
    id_cat = models.AutoField(primary_key=True)#ME PARECE QUE LOS ID ESTAN AL PEDO
    nombre_cat = models.CharField(max_length=100)
    desc_cat = models.TextField()
    def __unicode__(self):
        return self.nombre_cat


class subcategoria(models.Model):
    id_sc = models.AutoField(primary_key=True)
    nombre_sc = models.CharField(max_length=100)
    categoria =models.ForeignKey('categoria', related_name='C')#models.ManyToManyField(categoria)
    def __unicode__(self):
        return self.nombre_sc


class producto(models.Model):
    genero_choices = (('M', 'Masculino'),
            ('F', 'Femenino'),
            ('U', 'Unisex'))
    codigo = models.AutoField(primary_key=True)#models.IntegerField()
    nombre_producto = models.CharField(max_length=100)
    subcategoria = models.ForeignKey('subcategoria' ,related_name='SC')
    marca = models.CharField(max_length=100)
    stock = models.IntegerField(blank=False)
    genero = models.CharField(max_length=10, choices=genero_choices,default='M')
    precio = models.DecimalField(max_digits=9, decimal_places = 2)
    activo = models.BooleanField(default=False)
    descripcion = models.TextField()
    def __unicode__(self):
        return self.nombre_producto
