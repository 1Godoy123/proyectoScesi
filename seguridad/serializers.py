from rest_framework import serializers
from .models import Estudiante, Acceso

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['id', 'carnet', 'nombre', 'apellido', 'carrera', 'semestre', 'activo', 'fecha_registro']
        read_only_fields = ['fecha_registro']

class AccesoSerializer(serializers.ModelSerializer):
    estudiante_nombre = serializers.CharField(source='estudiante.nombre', read_only=True)
    estudiante_carnet = serializers.CharField(source='estudiante.carnet', read_only=True)

    class Meta:
        model = Acceso
        fields = ['id', 'estudiante', 'estudiante_nombre', 'estudiante_carnet', 
                 'fecha_hora', 'estado', 'mensaje', 'tipo_acceso']
        read_only_fields = ['fecha_hora']