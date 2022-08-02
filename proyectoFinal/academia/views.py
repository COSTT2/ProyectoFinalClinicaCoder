from django.shortcuts import render
from django.http import HttpResponse
from academia.models import Cursos, profesores
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def inicio(request):
    return render(request, "academia/inicio.html")

class listaCursos(ListView):
    model = Cursos
    template_name = "academia/lista_cursos.html"
    
class mostrarCursos(DetailView):
    model = Cursos
    template_name = "academia/informacion_cursos.html"
    
class crearCursos(CreateView):
    model = Cursos
    template_name = "academia/form_cursos.html"
    success_url = "/academia/cursos/lista"
    fields = ["titulo", "descripcion", "contenido", "imagen", "duracion"]
    
class editarCursos(UpdateView):
    model = Cursos
    template_name = "academia/form_cursos.html"
    success_url = "/academia/cursos/lista"
    fields = ["titulo", "descripcion", "contenido", "imagen", "duracion"]
 
class borrarCursos(DeleteView):
    model = Cursos
    template_name = "academia/borrar_cursos.html"
    success_url = "/academia/cursos/lista"

class listaProfesores(ListView):
    model = profesores
    template_name = "academia/lista_profesores.html"
    
class crearProfesores(CreateView):
    model = profesores
    template_name = "academia/form_profesores.html"
    success_url = "/academia/profesores/lista"
    fields = ["nombre", "apellido", "especialidad", "mail", "educacion", "imagen"]
    
class mostrarProfesores(DetailView):
    model = profesores
    template_name = "academia/informacion_profesores.html"
    
