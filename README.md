# Gestión de Formación

Plataforma web para la gestión de cursos, profesores, alumnos y matrículas, desarrollada con Django y PostgreSQL.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0.6-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-psycopg3-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)

---

## Funcionalidades

- Registro e inicio de sesión con modelo de usuario personalizado (alumno / profesor)
- Catálogo público de cursos con imagen, plazas y fechas
- Matriculación con control de plazas y duplicados
- Cancelación de matrículas con confirmación
- Dashboard privado del alumno con estadísticas
- Área privada con listado de cursos matriculados
- Menú dinámico según tipo de usuario
- Panel de administración personalizado con Jazzmin

---

## Tecnologías

| Tecnología | Versión |
|---|---|
| Python | 3.13 |
| Django | 6.0.6 |
| PostgreSQL | psycopg 3.3.4 |
| Bootstrap | django-bootstrap5 26.2 |
| Jazzmin | 3.0.4 |
| Pillow | 12.2.0 |
| python-dotenv | 1.2.2 |

---

## Estructura del proyecto

```
gestion_formacion/
├── config/          # Configuración principal (settings, urls, wsgi)
├── core/            # Página de inicio
├── usuarios/        # Modelo de usuario personalizado (alumno / profesor)
├── profesores/      # Perfil de profesor (especialidad, biografía, foto)
├── cursos/          # Cursos (nombre, descripción, plazas, fechas, imagen)
├── matriculas/      # Matrículas, dashboard y área privada del alumno
├── templates/       # Plantillas HTML globales
├── media/           # Archivos subidos (imágenes)
├── requirements.txt
└── manage.py
```

---

## Modelos principales

```
Usuario (AbstractUser)
 └── tipo: alumno | profesor

Profesor
 └── usuario (OneToOne)
 └── especialidad, teléfono, biografía, foto

Curso
 └── profesor (FK)
 └── nombre, descripción, plazas, fechas, imagen, activo

Matricula
 └── alumno (FK → Usuario)
 └── curso (FK → Curso)
 └── fecha_matricula
 └── unique_together: (alumno, curso)
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd gestion_formacion
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=<clave-secreta-django>
DEBUG=True
DB_NAME=<nombre-base-de-datos>
DB_USER=<usuario-postgresql>
DB_PASSWORD=<contraseña>
DB_HOST=localhost
DB_PORT=5432
```

> El archivo `.env` nunca debe subirse al repositorio.

### 5. Crear la base de datos

```bash
createdb <nombre-base-de-datos>
```

### 6. Aplicar migraciones

```bash
python manage.py migrate
```

### 7. Crear superusuario

```bash
python manage.py createsuperuser
```

### 8. Arrancar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## URLs principales

| URL | Descripción |
|---|---|
| `/` | Página de inicio |
| `/cursos/` | Catálogo de cursos |
| `/cursos/<id>/` | Detalle de un curso |
| `/matriculas/dashboard/` | Dashboard del alumno |
| `/matriculas/mis-cursos/` | Cursos matriculados |
| `/accounts/login/` | Inicio de sesión |
| `/admin/` | Panel de administración |

---

## Notas

- Idioma configurado en español (`es-es`).
- Las imágenes se almacenan en `media/`.
- En producción: `DEBUG=False` y configurar `ALLOWED_HOSTS` en `settings.py`.
