# Sistema de Control de Acceso

Sistema de control de acceso para estudiantes desarrollado con **Django** como proyecto final de Backend.

---

## Descripción del Proyecto

SCESI es un sistema backend para gestionar el ingreso y salida de estudiantes mediante el escaneo de carnet. Permite registrar accesos, controlar que no se pueda entrar dos veces sin salir, y notificar por correo electrónico cada evento.

---

## Características Principales

- **Registro de Acceso** con validación de entrada/salida
- Control inteligente: **No permite entrar dos veces** sin registrar salida
- Notificaciones por **correo electrónico** (Gmail)
- API RESTful con **Django REST Framework**
- Autenticación con **JWT** (JSON Web Tokens)
- Panel administrativo completo
- Frontend simple para demostración
- Buenas prácticas (Services, Serializers, etc.)

---

## Tecnologías Utilizadas

- **Backend**: Django 5/6 + Django REST Framework
- **Autenticación**: SimpleJWT
- **Base de Datos**: SQLite (fácil de cambiar a PostgreSQL)
- **Frontend**: HTML + Bootstrap 5 + JavaScript
- **Notificaciones**: Django Email (SMTP Gmail)
- **Entorno**: Python 3.13 + virtualenv

---

## 📁 Estructura del Proyecto
