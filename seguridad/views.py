from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Estudiante, Acceso
from .serializers import EstudianteSerializer, AccesoSerializer
from .services import AccesoService

@api_view(['GET'])
def api_root(request):
    return Response({
        "mensaje": "🚀 API Backend - Sistema de Control de Acceso (SCESI)",
        "version": "1.0",
        "endpoints": {
            "Registrar Acceso": "POST /api/seguridad/acceso/",
            "Lista Estudiantes": "GET /api/seguridad/estudiantes/",
            "Login JWT": "POST /api/token/",
            "Admin": "/admin/"
        }
    })
@api_view(['GET', 'POST'])
def estudiante_list_create(request):
    if request.method == 'GET':
        estudiantes = Estudiante.objects.all()
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EstudianteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([AllowAny])
def registrar_acceso(request):
    carnet = request.data.get('carnet')
    tipo_acceso = request.data.get('tipo_acceso', 'entrada')

    if not carnet:
        return Response({"error": "El campo 'carnet' es requerido"}, status=status.HTTP_400_BAD_REQUEST)

    acceso, exito = AccesoService.registrar_acceso(carnet, tipo_acceso)
    serializer = AccesoSerializer(acceso)

    if exito:
        return Response({
            "mensaje": "Acceso registrado correctamente",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            "mensaje": "Acceso denegado",
            "data": serializer.data
        }, status=status.HTTP_403_FORBIDDEN)