from django.urls import path, include
from academia.views import inicio, About
from academia.views import cursosLista, mostrarCurso, editarCurso, borrarCurso, crearCursos
from academia.views import listaProfesores, crearProfesores, mostrarProfesores, editarProfesores, borrarProfesores
from academia.views import edicionUsuario, SignUpView
from academia.views import peticion_login


from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("profesores/lista", listaProfesores.as_view(), name="listaProfesores"),
    path("profesores/crear", crearProfesores.as_view(), name="crearProfesores"),
    path("profesores/<pk>/", mostrarProfesores.as_view(), name="mostrarProfesores"),
    path("profesores/<pk>/editar", editarProfesores.as_view(), name="editar_profesores"),
    path("profesores/<pk>/borrar", borrarProfesores.as_view(), name="borrar_profesores"),
    path("cursos/lista", cursosLista.as_view(), name="cursos"),
    path("cursos/<pk>/", mostrarCurso.as_view(), name="mostrarCurso"),
    path("cursos/<pk>/editar", editarCurso.as_view(), name="editarCurso"),
    path("cursos/<pk>/borrar", borrarCurso.as_view(), name="borrarCurso"),
    path("cursos/crear", crearCursos.as_view(), name="crearCursos"),
    path("usuario/<pk>/editar", edicionUsuario.as_view(), name= "edicionUsuario"),
    path("login/", peticion_login, name = "login"),
    path("logout/", LogoutView.as_view(template_name="academia/logout.html"), name = "logout"),
    path("registro/", SignUpView.as_view(), name = "registro"),
    path('about/', About.as_view(), name="sobrenosotros"),
    
    
    
]
