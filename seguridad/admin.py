from django.contrib import admin
from .models import Estudiante, Acceso

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['carnet', 'nombre', 'apellido', 'carrera', 'semestre', 'activo']
    search_fields = ['carnet', 'nombre', 'apellido']
    list_filter = ['activo', 'carrera']

@admin.register(Acceso)
class AccesoAdmin(admin.ModelAdmin):
    list_display = ['estudiante', 'fecha_hora', 'estado', 'tipo_acceso']
    list_filter = ['estado', 'tipo_acceso', 'fecha_hora']
    search_fields = ['estudiante__nombre', 'estudiante__carnet']
    readonly_fields = ['fecha_hora']