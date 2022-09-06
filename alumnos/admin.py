from django.contrib import admin
from alumnos.models import Ubicacion, Curso, Alumnos

# Register your models here.
admin.site.register(Alumnos)
admin.site.register(Curso)
admin.site.register(Ubicacion)