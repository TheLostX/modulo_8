from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import AbstractUser 

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=50)

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=50)
    laboratorio = Laboratorio()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = Laboratorio()
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits= 2, decimal_places=2)
    p_venta = models.DecimalField(max_digits= 2, decimal_places=2)


