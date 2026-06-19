================================================================================
  GESTIÓN DE FORMACIÓN
  Plataforma web para la gestión de cursos, profesores, alumnos y matrículas
  Desarrollada con Django 6 + PostgreSQL + Bootstrap 5
================================================================================

DESCRIPCIÓN
-----------
Aplicación web desarrollada con Django para gestionar una academia de formación.
Permite registrarse, iniciar sesión, consultar el catálogo de cursos, matricularse,
gestionar matrículas y acceder a un dashboard privado con estadísticas personales.
El panel de administración utiliza Jazzmin para una interfaz moderna.

FUNCIONALIDADES
---------------
- Registro e inicio de sesión con modelo de usuario personalizado (alumno / profesor)
- Catálogo público de cursos con imagen, plazas y fechas
- Matriculación con control de plazas y duplicados
- Cancelación de matrículas con confirmación
- Dashboard privado del alumno con estadísticas
- Área privada con listado de cursos matriculados
- Menú dinámico según tipo de usuario
- Panel de administración personalizado con Jazzmin

TECNOLOGÍAS
-----------
  Python          3.13
  Django          6.0.6
  PostgreSQL      psycopg 3.3.4
  Bootstrap       django-bootstrap5 26.2
  Jazzmin         3.0.4
  Pillow          12.2.0
  python-dotenv   1.2.2

ESTRUCTURA DEL PROYECTO
-----------------------
gestion_formacion/
  config/          -> Configuración principal (settings, urls, wsgi)
  core/            -> Página de inicio
  usuarios/        -> Modelo de usuario personalizado (alumno / profesor)
  profesores/      -> Perfil de profesor (especialidad, biografía, foto)
  cursos/          -> Cursos (nombre, descripción, plazas, fechas, imagen)
  matriculas/      -> Matrículas, dashboard y área privada del alumno
  templates/       -> Plantillas HTML globales
  media/           -> Archivos subidos (imágenes)
  requirements.txt -> Dependencias del proyecto
  manage.py        -> CLI de Django

MODELOS PRINCIPALES
-------------------
  Usuario (AbstractUser)
    tipo: alumno | profesor

  Profesor
    usuario (OneToOne -> Usuario)
    especialidad, telefono, biografia, foto

  Curso
    profesor (ForeignKey -> Profesor)
    nombre, descripcion, plazas, fecha_inicio, fecha_fin, imagen, activo

  Matricula
    alumno (ForeignKey -> Usuario)
    curso  (ForeignKey -> Curso)
    fecha_matricula (auto)
    unique_together: (alumno, curso)   <- impide duplicados

INSTALACIÓN Y PUESTA EN MARCHA
-------------------------------
1. Clonar el repositorio:
      git clone <url-del-repositorio>
      cd gestion_formacion

2. Crear y activar el entorno virtual:
      python -m venv venv
      source venv/bin/activate        (Linux / Mac)
      venv\Scripts\activate           (Windows)

3. Instalar dependencias:
      pip install -r requirements.txt

4. Crear el archivo .env en la raíz del proyecto:
      SECRET_KEY=<clave-secreta-django>
      DEBUG=True
      DB_NAME=<nombre-base-de-datos>
      DB_USER=<usuario-postgresql>
      DB_PASSWORD=<contraseña>
      DB_HOST=localhost
      DB_PORT=5432

   IMPORTANTE: nunca subas el archivo .env al repositorio.

5. Crear la base de datos en PostgreSQL:
      createdb <nombre-base-de-datos>

6. Aplicar las migraciones:
      python manage.py migrate

7. Crear un superusuario para el panel de administración:
      python manage.py createsuperuser

8. Arrancar el servidor de desarrollo:
      python manage.py runserver

9. Abrir en el navegador:
      Aplicacion:       http://127.0.0.1:8000/
      Administracion:   http://127.0.0.1:8000/admin/

URLS PRINCIPALES
----------------
  /                            -> Página de inicio
  /cursos/                     -> Catálogo de cursos
  /cursos/<id>/                -> Detalle de un curso
  /matriculas/dashboard/       -> Dashboard del alumno
  /matriculas/mis-cursos/      -> Cursos matriculados
  /matriculas/matricular/<id>/ -> Matricularse en un curso
  /matriculas/cancelar/<id>/   -> Cancelar una matrícula
  /accounts/login/             -> Inicio de sesión
  /accounts/logout/            -> Cierre de sesión
  /admin/                      -> Panel de administración (Jazzmin)

NOTAS
-----
- Idioma configurado en español (es-es).
- Las imágenes se almacenan en la carpeta media/.
- En producción: DEBUG=False y configurar ALLOWED_HOSTS en settings.py.
- El archivo .env no debe incluirse en el control de versiones.

================================================================================
