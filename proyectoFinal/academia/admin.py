from django.contrib import admin
from academia.models import profesores, Curso, Inscripto, Portal, Article, Publisher

admin.site.register(profesores)
admin.site.register(Curso)
admin.site.register(Inscripto)
admin.site.register(Article)
admin.site.register(Portal)
admin.site.register(Publisher)