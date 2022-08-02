from django.urls import path
from panel.views import edicionUsuario, registroUsuario
urlpatterns = [
    path("user/<pk>/edit", edicionUsuario.as_view(), name= "edicionUsuario"),
    path("user/<pk>", registroUsuario.as_view(), name= "registroUsuario"),
]