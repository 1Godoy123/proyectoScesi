from django.db import models
from django.utils import timezone

class Estudiante(models.Model):
    carnet = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100, blank=True, null=True)
    semestre = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.carnet}"

    class Meta:
        verbose_name_plural = "Estudiantes"


class Acceso(models.Model):
    ESTADOS = [('APROBADO', 'Aprobado'), ('DENEGADO', 'Denegado')]

    estudiante = models.ForeignKey(Estudiante, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_hora = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='APROBADO')
    mensaje = models.TextField(blank=True, null=True)
    tipo_acceso = models.CharField(max_length=10, default='entrada')

    def __str__(self):
        return f"{self.estudiante} - {self.estado}"

    class Meta:
        verbose_name_plural = "Accesos"