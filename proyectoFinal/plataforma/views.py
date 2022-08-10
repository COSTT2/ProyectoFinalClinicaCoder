from django.shortcuts import render
from django.urls import reverse_lazy
from academia.models import Curso, Article, Portal, profesores
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from academia.views import BaseView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

@login_required
def plataforma(request):
    return render(request, "plataforma/plataforma.html")

def inicio(request):
    return render(request, "plataforma/inicio.html")

def config(request):
    return render(request, "plataforma/info_usuario.html")

@login_required
def admin(request):
    return render(request, "plataforma/admin.html")


class listaCursos(ListView):
    model = Curso
    template_name = "plataforma/listaCursos.html"
    
class infoCursos(DetailView):
    model = Curso
    template_name = "plataforma/info_cursos.html"
    
      
class PaginaInicio(LoginRequiredMixin, BaseView, ListView):
    
    queryset = Article.objects.all()
    template_name = "plataforma/plataforma.html"    
    context_object_name = "articles"
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title','short_content', 'author', 'image', 'image', 'date_published', "texto"]
    template_name = "plataforma/article_form.html"
    success_url = reverse_lazy("campus")
    
class ArticleDetailView(DetailView):

    model = Article
    context_object_name = "article"
    template_name = "plataforma/article_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portal'] = Portal.objects.order_by('date_updated').first()
        return context

class ArticleUpdateView(LoginRequiredMixin, BaseView, UpdateView):
    model = Article
    template_name = "plataforma/article_form.html"
    fields = ['title', 'short_content', 'author', 'image', 'image', 'date_published', "texto"]
    success_url = reverse_lazy('listaArticulos')

class ArticleDeleteView(LoginRequiredMixin, BaseView, DeleteView):
    model = Article
    template_name = "plataforma/article_confirm_delete.html"
    success_url = reverse_lazy('listaArticulos')
    
class ArticleList(LoginRequiredMixin, BaseView, ListView):
    
    queryset = Article.objects.all()
    template_name = "plataforma/article_list.html"    
    context_object_name = "articles"
    
class listaProfes(ListView):
    model = profesores
    template_name = "plataforma/profesores.html"
    
class listaUsuarios(ListView):
    model = User
    template_name = "plataforma/usuarios.html"



