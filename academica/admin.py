from django.contrib import admin
from .models import (
    Docente, Alumno, Curso, Inscripcion,
    Aula, CursoProfesor, Horario,
    Evaluacion, CalificacionEvaluacion, Mensaje
)
# En el archivo admin.py
from django.contrib import admin

admin.site.site_header = "Mi Portal de Administración"
admin.site.site_title = "Administración"
admin.site.index_title = "Bienvenido a la Administración"


admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Inscripcion)
admin.site.register(Aula)
admin.site.register(CursoProfesor)
admin.site.register(Horario)
admin.site.register(Evaluacion)
admin.site.register(CalificacionEvaluacion)
admin.site.register(Mensaje)