from django.contrib import admin

from AppCoder.models import Curso, Estudiantes, Profesor

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiantes)
admin.site.register(Profesor)