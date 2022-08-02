from django.urls import path
from academia.views import inicio
from academia.views import listaCursos, crearCursos, editarCursos, borrarCursos, mostrarCursos
from academia.views import listaProfesores, crearProfesores, mostrarProfesores

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("cursos/lista", listaCursos.as_view(), name="listaCursos"),
    path("cursos/<pk>/", mostrarCursos.as_view(), name="informacionCursos"),
    path("cursos/crear", crearCursos.as_view(), name="crearCursos"),
    path("cursos/<pk>/editar", editarCursos.as_view(), name="editarCursos"),
    path("cursos/<pk>/borrar", borrarCursos.as_view(), name="borrarCursos"),
    path("profesores/lista", listaProfesores.as_view(), name="listaProfesores"),
    path("profesores/crear", crearProfesores.as_view(), name="crearProfesores"),
    path("profesores/<pk>/", mostrarProfesores.as_view(), name="mostrarProfesores"),
]
