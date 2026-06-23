================================================================================
  GESTIÓN DE FORMACIÓN
  Plataforma web para la gestión de cursos, profesores, alumnos y matrículas
  Desarrollada con Django 6 + PostgreSQL + Bootstrap 5
================================================================================

DESCRIPCIÓN
-----------
Aplicación web desarrollada con Django para gestionar una academia de formación.
Permite registrarse, iniciar sesión, consultar el catálogo de cursos, matricularse,
gestionar matrículas y acceder a paneles privados con estadísticas personales.
El panel de administración utiliza Jazzmin para una interfaz moderna.

FUNCIONALIDADES
---------------
- Registro e inicio de sesión con modelo de usuario personalizado (alumno / profesor)
- Catálogo público de cursos con imagen, plazas y fechas
- Búsqueda de cursos por nombre o descripción
- Filtrado por profesor y paginación del catálogo (6 cursos por página)
- URLs amigables para SEO mediante slugs (generados automáticamente)
- Matriculación con control de plazas y duplicados
- Cancelación de matrículas con confirmación
- Dashboard privado del alumno con estadísticas personales
- Panel privado del profesor con estadísticas por curso
- Gestión de cursos propios (crear, editar, eliminar) para profesores
- Menú dinámico según tipo de usuario (alumno / profesor)
- Panel de administración personalizado con Jazzmin
- Nombres en español en el panel de administración
- Bordes visibles en todos los campos de formulario
- CSS personalizado para el panel de administración
- Decorador @profesor_required para proteger vistas privadas
- Vistas de cursos con Class Based Views (CBV) y Mixins de permisos

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
  usuarios/        -> Modelo de usuario personalizado + decoradores de permisos
  profesores/      -> Perfil de profesor + panel privado con estadísticas
  cursos/          -> Cursos: modelos CBV, formularios Bootstrap, admin
  matriculas/      -> Matrículas, dashboard alumno y área privada
  templates/       -> Plantillas HTML globales
  static/css/      -> CSS personalizado (admin_custom.css)
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
    nombre (db_index), slug (unique), descripcion
    plazas, fecha_inicio, fecha_fin, imagen, activo
    verbose_name = 'Curso' / verbose_name_plural = 'Cursos'

  Matricula
    alumno (ForeignKey -> Usuario)
    curso  (ForeignKey -> Curso)
    fecha_matricula (auto)
    unique_together: (alumno, curso)   <- impide duplicados
    verbose_name = 'Matrícula' / verbose_name_plural = 'Matrículas'

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
  /                              -> Página de inicio
  /cursos/                       -> Catálogo (búsqueda, filtro y paginación)
  /cursos/<slug>/                -> Detalle de un curso
  /cursos/nuevo/                 -> Crear curso (solo profesores)
  /cursos/<slug>/editar/         -> Editar curso (solo profesores)
  /cursos/<slug>/eliminar/       -> Eliminar curso (solo profesores)
  /matriculas/matricular/<id>/   -> Matricularse en un curso
  /matriculas/cancelar/<id>/     -> Cancelar una matrícula
  /matriculas/mis-cursos/        -> Cursos matriculados del alumno
  /matriculas/dashboard/         -> Dashboard privado del alumno
  /profesores/dashboard/         -> Panel privado del profesor
  /profesores/mis-cursos/        -> Cursos del profesor con estadísticas
  /usuarios/registro/            -> Registro de nuevo usuario
  /accounts/login/               -> Inicio de sesión
  /accounts/logout/              -> Cierre de sesión
  /admin/                        -> Panel de administración (Jazzmin)

NOTAS
-----
- Idioma configurado en español (es-es).
- Las imágenes se almacenan en la carpeta media/.
- Los slugs se generan automáticamente a partir del nombre del curso.
- Las vistas de cursos utilizan Class Based Views (CBV).
- En producción: DEBUG=False y configurar ALLOWED_HOSTS en settings.py.
- El archivo .env no debe incluirse en el control de versiones.
- Los archivos __pycache__ y *.pyc están excluidos del repositorio.

================================================================================
