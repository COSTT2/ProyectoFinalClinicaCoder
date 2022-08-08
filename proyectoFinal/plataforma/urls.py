from django.urls import path
from plataforma.views import plataforma

urlpatterns = [
    path("campus/", plataforma, name= "campus"),
]