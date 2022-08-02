from unittest.util import _MAX_LENGTH
from django.db import models
from ckeditor.fields import RichTextField

class Cursos(models.Model):
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to="articulos", null=True, blank=True)
    duracion = models.Charfield(max_lenght=40)
    
class profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    mail = models.EmailField(max_length=100)
    educacion = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="articulos", null=True, blank=True)
