================================================================================
  GESTIÓN DE FORMACIÓN
  Aplicación web para la gestión de cursos, profesores y alumnos
================================================================================

DESCRIPCIÓN
-----------
Aplicación web desarrollada con Django para gestionar una academia de formación.
Permite administrar cursos, profesores, alumnos y matrículas desde un panel de
control con interfaz moderna (Jazzmin).

TECNOLOGÍAS
-----------
- Python 3.13
- Django 6.0.6
- PostgreSQL (psycopg 3.3.4)
- Bootstrap 5 (django-bootstrap5 26.2)
- Jazzmin 3.0.4 (tema para el panel de administración)
- Pillow 12.2.0 (gestión de imágenes)
- python-dotenv 1.2.2

ESTRUCTURA DEL PROYECTO
-----------------------
gestion_formacion/
├── config/          -> Configuración principal de Django (settings, urls, wsgi)
├── core/            -> App principal: página de inicio
├── usuarios/        -> Gestión de usuarios (modelo personalizado: alumno/profesor)
├── profesores/      -> Gestión de profesores (perfil, especialidad, foto)
├── cursos/          -> Gestión de cursos (nombre, descripción, plazas, fechas, imagen)
├── matriculas/      -> Gestión de matrículas (alumnos inscritos en cursos)
├── templates/       -> Plantillas HTML globales
├── media/           -> Archivos subidos (imágenes de cursos y profesores)
├── requirements.txt -> Dependencias del proyecto
└── manage.py        -> CLI de Django

MODELOS PRINCIPALES
-------------------
- Usuario: extiende AbstractUser con tipo (alumno / profesor)
- Profesor: vinculado a Usuario, con especialidad, teléfono, biografía y foto
- Curso: nombre, descripción, profesor, fechas, plazas, imagen y estado activo

INSTALACIÓN Y PUESTA EN MARCHA
-------------------------------
1. Clonar el repositorio:
   git clone <url-del-repositorio>
   cd gestion_formacion

2. Crear y activar el entorno virtual:
   python -m venv venv
   source venv/bin/activate        # Linux / Mac
   venv\Scripts\activate           # Windows

3. Instalar dependencias:
   pip install -r requirements.txt

4. Crear el archivo .env en la raíz del proyecto con las siguientes variables:
   SECRET_KEY=<clave-secreta-django>
   DEBUG=True
   DB_NAME=<nombre-base-de-datos>
   DB_USER=<usuario-postgresql>
   DB_PASSWORD=<contraseña-postgresql>
   DB_HOST=localhost
   DB_PORT=5432

5. Crear la base de datos en PostgreSQL:
   createdb <nombre-base-de-datos>

6. Aplicar las migraciones:
   python manage.py migrate

7. Crear un superusuario para el panel de administración:
   python manage.py createsuperuser

8. Arrancar el servidor de desarrollo:
   python manage.py runserver

9. Abrir en el navegador:
   - Aplicación:          http://127.0.0.1:8000/
   - Panel de admín:      http://127.0.0.1:8000/admin/

URLS PRINCIPALES
----------------
/                   -> Página de inicio
/cursos/            -> Listado de cursos activos
/cursos/<id>/       -> Detalle de un curso
/usuarios/          -> Gestión de perfil de usuario
/accounts/login/    -> Inicio de sesión
/accounts/logout/   -> Cierre de sesión
/admin/             -> Panel de administración (Jazzmin)

NOTAS
-----
- El idioma de la aplicación está configurado en español (es-es).
- Las imágenes de cursos y profesores se almacenan en la carpeta media/.
- En producción: establecer DEBUG=False y configurar ALLOWED_HOSTS en settings.py.
- No incluir el archivo .env en el control de versiones.

================================================================================
