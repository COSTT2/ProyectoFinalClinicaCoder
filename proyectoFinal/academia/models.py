from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

    
class profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    mail = models.EmailField(max_length=100)
    educacion = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="articulos", null=True, blank=True)
    
class Curso(models.Model):
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    contenido = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="articulos", null=True, blank=True)
    duracion = models.CharField(max_length=40)
    

class Publisher(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    avatar = models.ImageField(upload_to="avatars", null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Article(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=180)
    image = models.ImageField(upload_to="articles", null=True, blank=True)
    author = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()
    texto = models.CharField(max_length=500, default="")


class Portal(models.Model):
    name = models.CharField(max_length=20)
    social_network_one = models.URLField(null=True)
    social_network_two = models.URLField(null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
