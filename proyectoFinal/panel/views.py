from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy

class edicionUsuario(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name ="perfil_usuario/usuario_form.html"
    fields = ["email", "primer_nombre", "apellido"]
    
    def get_success_url(self):
        return reverse_lazy("informacionUsuario", kwargs={"pk": self.request.user.id})
    
    def test_func(self):
        return self.request.user.id == int(self.kwargs["pk"])
    
class registroUsuario(SuccessMessageMixin, CreateView):
  template_name = 'academia/crear_cuenta_form.html'
  success_url = reverse_lazy()
  form_class = UserCreationForm
  success_message = "Se ha creado tu perfil"