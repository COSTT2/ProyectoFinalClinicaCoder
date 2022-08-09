from ast import Return
from pyexpat.errors import messages
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from academia.models import Curso, profesores
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from academia.forms import UserRegisterForm
from django.views.generic import TemplateView, View
from academia.models import Article, Portal



def inicio(request):
    return render(request,"academia/inicio.html")

class BaseView(View):

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portal'] = Portal.objects.order_by('date_updated').first()
        return context    

class About(BaseView, TemplateView):
    template_name = "academia/sobrenosotros.html"

# --- views profesores ---

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

class editarProfesores(UpdateView):
    model = profesores
    template_name = "academia/form_profesores.html"
    success_url = "/academia/profesores/lista"
    fields = ["nombre", "apellido", "especialidad", "mail", "educacion", "imagen"]

class borrarProfesores(DeleteView):
    model = profesores
    template_name = "academia/borrar_profesores.html"
    success_url = "/academia/profesores/lista"
    
# --- views cursos ---
    
class cursosLista(ListView):
    model = Curso
    template_name = "academia/cursos.html"

class mostrarCurso(DetailView):
    model = Curso
    template_name = "academia/informacion_cursos.html"
    
class editarCurso(UpdateView):
    model = Curso
    template_name = "plataforma/form_cursos.html"
    success_url = "/plataforma/listaCursos/"
    fields = ["titulo", "descripcion", "contenido", "imagen", "duracion"]
    
class borrarCurso(DeleteView):
    model = Curso
    template_name = "plataforma/borrar_cursos.html"
    success_url = "/plataforma/listaCursos/"

class crearCursos(CreateView):
    model = Curso
    template_name = "plataforma/form_cursos.html"
    success_url = "/plataforma/listaCursos/"
    fields = ["titulo", "descripcion", "contenido", "imagen", "duracion"]
    
# --- views usuarios ---
@login_required
def dummy(request):
    render(request, "")
    
class edicionUsuario(LoginRequiredMixin, UpdateView):
    model = User
    template_name ="plataforma/usuario_form.html"
    fields = ["username", "email", "first_name", "last_name"]
    
    def get_success_url(self):
        return reverse_lazy("config", kwargs={"pk": self.request.user.id})
    
class perfilUsuario(LoginRequiredMixin, UserPassesTestMixin, DetailView):

    model = User
    template_name = "plataforma/info_usuario.html"

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

    
class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'academia/register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Se creo tu perfil satisfactoriamente"
    
def peticion_login(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contrasena)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido {usuario}")
                return redirect("inicio")
            
            else:
                messages.error(request, "La contraseña o nombre de usuario son incorrectos")
                return render(request, "academia/login.html")
            
        else: 
                messages.error(request, "Ups! algo salió mal")
                return render(request, "academia/login.html")
    
    form = AuthenticationForm()
    
    return render(request,"academia/login.html", {"form":form} )

