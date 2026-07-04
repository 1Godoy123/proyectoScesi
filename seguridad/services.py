from django.utils import timezone
from .models import Estudiante, Acceso

class AccesoService:

    @staticmethod
    def registrar_acceso(carnet: str, tipo_acceso: str = "entrada"):
        try:
            estudiante = Estudiante.objects.get(carnet=carnet, activo=True)
            ultimo_acceso = Acceso.objects.filter(estudiante=estudiante).order_by('-fecha_hora').first()

            estado = "APROBADO"
            mensaje = ""

            if tipo_acceso == "entrada":
                if ultimo_acceso and ultimo_acceso.tipo_acceso == "entrada":
                    estado = "DENEGADO"
                    mensaje = "El estudiante ya está dentro. Debe registrar salida primero."
                else:
                    mensaje = "Entrada registrada correctamente"
            else:  # salida
                if ultimo_acceso and ultimo_acceso.tipo_acceso == "salida":
                    estado = "DENEGADO"
                    mensaje = "El estudiante ya había registrado salida."
                else:
                    mensaje = "Salida registrada correctamente"

            acceso = Acceso.objects.create(
                estudiante=estudiante,
                estado=estado,
                mensaje=mensaje,
                tipo_acceso=tipo_acceso
            )
            AccesoService.enviar_notificacion_email(acceso)

            return acceso, (estado == "APROBADO")

        except Estudiante.DoesNotExist:
            acceso = Acceso.objects.create(
                estudiante=None,
                estado="DENEGADO",
                mensaje="Carnet no encontrado o inactivo",
                tipo_acceso=tipo_acceso
            )
            AccesoService.enviar_notificacion_email(acceso)
            return acceso, False

    @staticmethod
    def enviar_notificacion_email(acceso):
        try:
            nombre = f"{acceso.estudiante.nombre} {acceso.estudiante.apellido}" if acceso.estudiante else "Desconocido"
            carnet = acceso.estudiante.carnet if acceso.estudiante else "N/A"

            from django.core.mail import send_mail
            send_mail(
                subject=f'🔔 Acceso {acceso.estado} - {nombre}',
                message=f"""
                Nuevo registro de acceso:

                Nombre: {nombre}
                Carnet: {carnet}
                Hora: {acceso.fecha_hora.strftime('%H:%M:%S')}
                Tipo: {acceso.tipo_acceso.upper()}
                Estado: {acceso.estado}
                Mensaje: {acceso.mensaje}
                """,
                from_email=None,
                recipient_list=['godoymontanojherson@gmail.com'],
                fail_silently=True,
            )
        except:
            pass