from django.urls import path
from plataforma.views import plataforma, listaCursos, infoCursos, PaginaInicio, ArticleCreateView, ArticleDetailView, ArticleList
from plataforma.views import ArticleUpdateView, ArticleDeleteView
from academia.views import edicionUsuario, perfilUsuario, perfilUsuario
from django.contrib.auth import views as auth_views
from plataforma.views import inicio

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("campus/", PaginaInicio.as_view(), name= "campus"),
    path("configuracion/<pk>/", perfilUsuario.as_view() , name="config"),
    path("listaCursos/", listaCursos.as_view(), name= "listaCursos"),
    path("infoCursos/<pk>/", infoCursos.as_view(), name="infoCursos"),
    path("usuario/<pk>/editar", edicionUsuario.as_view(), name="editarUsuario"),
    path("usuario/<pk>", perfilUsuario.as_view(), name="perfil"),
    path('articulos/crear', ArticleCreateView.as_view(), name ="crearArticulos"),
    path('article/<pk>/', ArticleDetailView.as_view(), name='detalleArticulo'),
    path("administracion/articulos/lista", ArticleList.as_view(), name="listaArticulos"),
    path('articulo/<pk>/editar', ArticleUpdateView.as_view(), name ="editarArticulo"),
    path('articulo/<pk>/borrar', ArticleDeleteView.as_view(), name ="borrarArticulo"),

]