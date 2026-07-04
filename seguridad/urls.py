from django.urls import path
from .views import estudiante_list_create, registrar_acceso

urlpatterns = [
    path('estudiantes/', estudiante_list_create, name='estudiantes-list-create'),
    path('acceso/', registrar_acceso, name='registrar-acceso'),    
]