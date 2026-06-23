# Guía Completa del Proyecto — Gestión de Formación con Django

> Documento pensado para alguien que está aprendiendo a programar.
> Aquí encontrarás explicaciones de todo: desde qué es Python hasta
> cómo funciona cada línea de código que hemos escrito.

---

# PARTE 0 — Conceptos básicos antes de empezar

Antes de ver el código, necesitas entender el vocabulario. Si ya sabes
algo de esto, puedes saltarte lo que conozcas.

---

## ¿Qué es Python?

Python es un **lenguaje de programación**. Un lenguaje de programación es
un idioma que los humanos usamos para darle instrucciones a un ordenador.

El ordenador solo entiende ceros y unos. Python actúa como traductor:
tú escribes instrucciones en Python (que son legibles para un humano),
y Python las traduce a algo que el ordenador puede ejecutar.

Ejemplo de instrucción en Python:

```python
print("Hola mundo")
```

Esto le dice al ordenador: "escribe en pantalla el texto Hola mundo".

---

## ¿Qué es Django?

Django es un **framework web** escrito en Python.

¿Qué es un framework? Imagina que quieres construir una casa.
Podrías fabricar tú mismo los ladrillos, las puertas, las ventanas...
o podrías comprarlos ya hechos y solo ensamblarlos.

Django es como una caja de herramientas ya construidas para hacer
páginas web. Incluye:
- Sistema de base de datos
- Sistema de usuarios y contraseñas
- Panel de administración
- Sistema de plantillas HTML
- Gestión de URLs
- Y mucho más

Sin Django, tendrías que programar todo eso tú solo desde cero.

---

## ¿Qué es una base de datos?

Una base de datos es como una hoja de cálculo Excel muy potente donde
se guarda toda la información de forma permanente.

Ejemplo: cuando un alumno se registra en nuestra plataforma, su nombre
y contraseña se guardan en la base de datos. Cuando vuelve a iniciar
sesión, Django busca sus datos ahí.

Nosotros usamos **PostgreSQL**, que es uno de los sistemas de bases de
datos más profesionales y utilizados en el mundo.

---

## ¿Qué es HTML?

HTML es el lenguaje con el que se construyen las páginas web que ves
en el navegador. Define la estructura: qué hay un título, un párrafo,
una tabla, un botón, etc.

```html
<h1>Bienvenido</h1>
<p>Esta es una página web.</p>
<button>Haz clic aquí</button>
```

---

## ¿Qué es Bootstrap?

Bootstrap es una librería de estilos visuales. Con HTML normal las páginas
quedan feas y sin diseño. Bootstrap añade colores, tipografías bonitas,
botones con estilo, tablas formateadas, etc.

Se usa añadiendo clases CSS a las etiquetas HTML:

```html
<!-- Sin Bootstrap: botón feo -->
<button>Guardar</button>

<!-- Con Bootstrap: botón verde bonito -->
<button class="btn btn-success">Guardar</button>
```

---

## ¿Qué es un entorno virtual (venv)?

Imagina que tienes dos proyectos en el mismo ordenador:
- Proyecto A necesita Django versión 4
- Proyecto B necesita Django versión 6

Si instalas Django globalmente en el ordenador, no puedes tener las dos
versiones a la vez. La solución es crear un **entorno virtual** para cada
proyecto: una carpeta aislada donde se instalan las librerías solo para
ese proyecto.

```bash
python -m venv venv        # Crea la carpeta venv/
source venv/bin/activate   # Activa el entorno (Linux/Mac)
```

Cuando el entorno está activado, verás `(venv)` al principio de la línea
en la terminal.

---

## ¿Qué es el archivo .env?

El archivo `.env` guarda información **secreta** que no debe estar en el
código ni en GitHub:
- La clave secreta de Django
- La contraseña de la base de datos
- Configuraciones que cambian entre desarrollo y producción

```
SECRET_KEY=mi-clave-super-secreta
DEBUG=True
DB_PASSWORD=mi-contraseña
```

Este archivo **nunca** se sube a GitHub. Si alguien roba tu SECRET_KEY,
puede falsificar sesiones de usuario y atacar tu aplicación.

---

## ¿Qué es Git y GitHub?

**Git** es un sistema que guarda el historial de cambios de tu código.
Es como el "control de cambios" de Word, pero para programadores.

Cada vez que haces un `git commit`, guardas una foto del estado actual
del proyecto. Puedes volver atrás en el tiempo si algo sale mal.

**GitHub** es una web donde puedes subir tu repositorio Git para:
- Tenerlo como copia de seguridad
- Trabajar en equipo
- Mostrar tu trabajo a otros

Comandos básicos que hemos usado:
```bash
git add archivo.py        # Prepara el archivo para guardar
git commit -m "mensaje"  # Guarda una foto con un mensaje descriptivo
git push                 # Sube los cambios a GitHub
```

---

## ¿Cómo funciona una página web? (El ciclo petición-respuesta)

Cuando escribes `http://127.0.0.1:8000/cursos/` en el navegador, ocurre esto:

```
1. TU NAVEGADOR
   "Quiero ver /cursos/"
        ↓
2. DJANGO RECIBE LA PETICIÓN
   "¿Qué URL es /cursos/? Busco en mis URLs..."
        ↓
3. DJANGO ENCUENTRA LA VISTA
   "La URL /cursos/ corresponde a ListaCursosView"
        ↓
4. LA VISTA CONSULTA LA BASE DE DATOS
   "Dame todos los cursos activos"
        ↓
5. LA VISTA PREPARA LA RESPUESTA
   "Tengo estos cursos, los meto en la plantilla HTML"
        ↓
6. DJANGO DEVUELVE EL HTML AL NAVEGADOR
        ↓
7. TU NAVEGADOR MUESTRA LA PÁGINA
```

Este ciclo se llama **petición-respuesta** (request-response en inglés).
En Django:
- La petición es el objeto `request`
- La respuesta es lo que devuelve la vista (`render`, `redirect`, etc.)

---

# PARTE 1 — Estructura del proyecto

## ¿Qué es una "app" en Django?

Django organiza el código en **aplicaciones** (apps). Cada app es una
carpeta que agrupa modelos, vistas y URLs relacionados con un tema.

Nuestro proyecto tiene estas apps:

```
gestion_formacion/          ← Carpeta raíz del proyecto
│
├── config/                 ← Configuración de Django (no es una app)
│   ├── settings.py         ← Configuración global (base de datos, apps instaladas...)
│   ├── urls.py             ← URLs principales del proyecto
│   └── wsgi.py             ← Punto de entrada para el servidor web
│
├── core/                   ← App: página de inicio
├── usuarios/               ← App: registro, login, modelo de usuario
├── profesores/             ← App: perfil de profesor, panel privado
├── cursos/                 ← App: catálogo, detalle, crear/editar/eliminar cursos
├── matriculas/             ← App: matriculación, dashboard del alumno
│
├── templates/              ← Todas las plantillas HTML
├── media/                  ← Imágenes subidas por los usuarios
├── requirements.txt        ← Lista de librerías necesarias
└── manage.py               ← Herramienta de comandos de Django
```

## ¿Qué hay dentro de cada app?

Cada app sigue la misma estructura:

```
cursos/
├── models.py     ← Define las tablas de la base de datos
├── views.py      ← Lógica de qué hacer cuando alguien visita una URL
├── urls.py       ← Mapeo entre URLs y vistas
├── admin.py      ← Cómo aparece esta app en el panel de administración
├── forms.py      ← Formularios HTML generados desde Python
└── apps.py       ← Configuración de la app (nombre, etc.)
```

---

## El archivo settings.py

Es el archivo de configuración central de Django. Las partes más importantes:

```python
INSTALLED_APPS = [
    'jazzmin',          # Tema del admin
    'django.contrib.admin',   # Panel de administración
    'django.contrib.auth',    # Sistema de autenticación
    ...
    'core',             # Nuestras apps
    'usuarios',
    'profesores',
    'cursos',
    'matriculas',
]
```

`INSTALLED_APPS` le dice a Django qué aplicaciones están activas.
Si una app no está aquí, Django no la conoce.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),      # Lee del archivo .env
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}
```

`DATABASES` le dice a Django dónde está la base de datos y cómo conectarse.
Usamos `os.getenv()` para leer los datos del archivo `.env` (no los
ponemos directamente en el código por seguridad).

```python
AUTH_USER_MODEL = 'usuarios.Usuario'
```

Le dice a Django que nuestro modelo de usuario personalizado es `Usuario`
dentro de la app `usuarios`, en lugar del modelo por defecto de Django.

---

# PARTE 2 — Los modelos (la base de datos)

## ¿Qué es un modelo?

Un modelo en Django es una clase Python que representa una tabla
en la base de datos.

Cuando escribes esto en Python:

```python
class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    plazas = models.PositiveIntegerField(default=20)
```

Django entiende que hay que crear una tabla en la base de datos así:

```
Tabla: cursos_curso
┌────────────────────┬──────────┐
│ nombre             │ plazas   │
├────────────────────┼──────────┤
│ Python Básico      │ 20       │
│ Django Avanzado    │ 15       │
│ Docker             │ 25       │
└────────────────────┴──────────┘
```

Cada **campo del modelo** (`CharField`, `IntegerField`, etc.) corresponde
a una **columna de la tabla**.
Cada **objeto** que guardamos corresponde a una **fila de la tabla**.

---

## Tipos de campos más usados

| Campo | Para qué sirve | Ejemplo |
|---|---|---|
| `CharField` | Texto corto | nombre, email |
| `TextField` | Texto largo | descripción, biografía |
| `IntegerField` | Número entero | edad, cantidad |
| `PositiveIntegerField` | Número entero positivo | plazas |
| `BooleanField` | Verdadero/Falso | activo, publicado |
| `DateField` | Fecha (día/mes/año) | fecha_inicio |
| `DateTimeField` | Fecha y hora | fecha_matricula |
| `ImageField` | Imagen subida | foto, imagen |
| `SlugField` | Texto para URLs | python-basico |
| `ForeignKey` | Relación con otro modelo | profesor |

---

## Modelo Usuario (`usuarios/models.py`)

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPO_USUARIO = (
        ('alumno', 'Alumno'),
        ('profesor', 'Profesor'),
    )
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO,
        default='alumno'
    )
```

**¿Qué es AbstractUser?**
Django ya tiene un modelo de usuario con username, email, password, etc.
En lugar de crear uno desde cero, **heredamos** de él con `AbstractUser`.
Heredar significa "coge todo lo que ya tiene AbstractUser y añádele esto".

Lo que añadimos: un campo `tipo` que puede ser `'alumno'` o `'profesor'`.

**choices**: limita los valores posibles del campo. El usuario no puede
tener tipo `'director'` o `'conserje'`, solo `'alumno'` o `'profesor'`.

---

## Modelo Profesor (`profesores/models.py`)

```python
class Profesor(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profesor'
    )
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    biografia = models.TextField(blank=True)
    foto = models.ImageField(upload_to='profesores/', blank=True, null=True)
```

**OneToOneField**: relación uno a uno. Cada profesor tiene exactamente
un usuario, y cada usuario puede ser exactamente un profesor.

Es como un DNI: cada persona tiene un solo DNI y cada DNI pertenece
a una sola persona.

**on_delete=models.CASCADE**: si se borra el usuario, se borra también
el perfil de profesor. "En cascada".

**related_name='profesor'**: permite acceder al perfil desde el usuario:
```python
request.user.profesor  # Accede al perfil del profesor del usuario actual
```

**blank=True**: el campo puede estar vacío en los formularios.
**null=True**: el campo puede ser NULL en la base de datos.

---

## Modelo Curso (`cursos/models.py`)

```python
class Curso(models.Model):
    nombre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    descripcion = models.TextField()
    profesor = models.ForeignKey(
        Profesor,
        on_delete=models.PROTECT,
        related_name='cursos'
    )
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    plazas = models.PositiveIntegerField(default=20)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='cursos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**ForeignKey** (clave foránea): un curso tiene un solo profesor, pero un
profesor puede tener muchos cursos. Es una relación "muchos a uno".

```
Profesor Ana
    ├── Curso Python Básico
    ├── Curso Python Avanzado
    └── Curso Django
```

**on_delete=models.PROTECT**: impide borrar un profesor si tiene cursos.
Si intentas borrar a Ana y tiene cursos, Django lanzará un error.

**db_index=True**: crea un índice en la base de datos para ese campo.
Sin índice, buscar "Python" entre 10.000 cursos revisa los 10.000 uno a uno.
Con índice, va directamente a los que contienen "Python". Mucho más rápido.

**auto_now_add=True**: guarda automáticamente la fecha/hora de creación.
**auto_now=True**: actualiza automáticamente la fecha/hora cada vez que se guarda.

**El método save():**
```python
def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.nombre)
    super().save(*args, **kwargs)
```

`save()` se ejecuta automáticamente cuando guardamos un curso.
Si el slug está vacío, lo generamos con `slugify()`:
- "Python Básico" → "python-basico"
- "Django para Principiantes" → "django-para-principiantes"

`super().save()` llama al método save() original de Django para que
realmente guarde en la base de datos.

---

## Modelo Matricula (`matriculas/models.py`)

```python
class Matricula(models.Model):
    alumno = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )
    fecha_matricula = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('alumno', 'curso')
```

Este modelo es la "tabla intermedia" que conecta alumnos con cursos.

**¿Por qué necesitamos esta tabla?**

Un alumno puede estar en varios cursos, y un curso puede tener varios alumnos.
Esto se llama relación **Muchos a Muchos** (N:M).

```
Alumno Ana  ──┬── Curso Python
              └── Curso Django

Alumno Juan ──┬── Curso Python
              └── Curso Docker

Curso Python ──┬── Alumno Ana
               └── Alumno Juan
```

En la base de datos se representa así:
```
Tabla matriculas_matricula:
┌────────────┬──────────┬─────────────────────┐
│ alumno_id  │ curso_id │ fecha_matricula      │
├────────────┼──────────┼─────────────────────┤
│ 1 (Ana)    │ 1 (Py)   │ 2026-01-15 10:30:00 │
│ 1 (Ana)    │ 2 (Dj)   │ 2026-01-20 09:15:00 │
│ 2 (Juan)   │ 1 (Py)   │ 2026-01-16 11:00:00 │
└────────────┴──────────┴─────────────────────┘
```

**unique_together**: la combinación de alumno+curso debe ser única.
Impide que Ana se matricule dos veces en Python.

---

## ¿Qué son las migraciones?

Cuando cambias un modelo en Python, la base de datos no se actualiza sola.
Las migraciones son el puente entre tu código Python y la base de datos real.

```bash
python manage.py makemigrations  # Crea el archivo de migración
python manage.py migrate         # Aplica los cambios a la base de datos
```

`makemigrations` genera un archivo en `migraciones/` que describe los cambios.
`migrate` ejecuta esos cambios en PostgreSQL.

Es como tener una lista de instrucciones: "añade esta columna", "crea esta tabla".

---

# PARTE 3 — Las vistas (la lógica)

## ¿Qué es una vista?

Una vista es la función (o clase) que recibe la petición del navegador,
hace lo que haga falta (consultar la base de datos, procesar un formulario...)
y devuelve una respuesta (normalmente una página HTML).

---

## FBV — Function Based Views (Vistas basadas en funciones)

La forma más simple de escribir una vista:

```python
def lista_cursos(request):
    cursos = Curso.objects.filter(activo=True)
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})
```

- `request`: contiene toda la información de la petición (quién hace la petición,
  qué método HTTP usa GET/POST, qué datos envía, etc.)
- `Curso.objects.filter(activo=True)`: consulta a la base de datos
- `render()`: combina la plantilla HTML con los datos y devuelve el HTML final
- `{'cursos': cursos}`: diccionario de datos que se pasan a la plantilla.
  En la plantilla puedes usar `{{ cursos }}` para mostrarlos.

---

## CBV — Class Based Views (Vistas basadas en clases)

Django tiene vistas genéricas que hacen el trabajo más común automáticamente:

```python
class ListaCursosView(ListView):
    model = Curso
    template_name = 'cursos/lista_cursos.html'
    context_object_name = 'cursos'
    paginate_by = 6
```

Esto hace exactamente lo mismo que la FBV de arriba, pero Django lo hace
solo. `ListView` ya sabe cómo consultar todos los objetos del modelo y
pasarlos a la plantilla.

**¿Cuándo usar FBV y cuándo CBV?**
- **FBV**: cuando la lógica es muy específica o compleja
- **CBV**: para operaciones estándar (listar, ver detalle, crear, editar, borrar)

---

## El ORM de Django

ORM significa "Object Relational Mapper". Es el sistema que traduce
código Python a consultas SQL automáticamente.

Sin ORM tendrías que escribir SQL:
```sql
SELECT * FROM cursos_curso WHERE activo = TRUE ORDER BY fecha_inicio;
```

Con el ORM de Django escribes Python:
```python
Curso.objects.filter(activo=True).order_by('fecha_inicio')
```

**Consultas más usadas:**

```python
# Todos los cursos
Curso.objects.all()

# Cursos activos
Curso.objects.filter(activo=True)

# Cursos NO activos
Curso.objects.exclude(activo=True)

# Un solo curso por ID (error 404 si no existe)
get_object_or_404(Curso, pk=1)

# Ordenar
Curso.objects.order_by('fecha_inicio')       # Ascendente
Curso.objects.order_by('-fecha_inicio')      # Descendente (el - invierte)

# Contar
Curso.objects.filter(activo=True).count()

# El primero
Curso.objects.order_by('fecha_inicio').first()

# Crear
curso = Curso.objects.create(nombre='Python', plazas=20)

# Buscar o crear (devuelve objeto y si fue creado)
matricula, creada = Matricula.objects.get_or_create(alumno=user, curso=curso)

# Buscar con texto (sin distinguir mayúsculas)
Curso.objects.filter(nombre__icontains='python')
# Encuentra: "Python Básico", "PYTHON", "python avanzado"
```

---

## Decoradores

Un decorador es algo que se pone encima de una función para añadirle
comportamiento extra sin modificar la función en sí.

```python
@login_required
def mis_cursos(request):
    ...
```

El `@login_required` hace que antes de ejecutar `mis_cursos`, Django
compruebe si el usuario está autenticado. Si no lo está, lo redirige
al login. Si lo está, ejecuta la vista normalmente.

Es como un guardia de seguridad que comprueba si tienes acceso antes
de dejarte pasar.

**Nuestro decorador personalizado:**

```python
def profesor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.tipo != 'profesor':
            messages.error(request, 'Acceso denegado.')
            return redirect('inicio')
        return view_func(request, *args, **kwargs)
    return wrapper
```

Este decorador hace dos comprobaciones:
1. ¿Está autenticado? Si no → login
2. ¿Es profesor? Si no → inicio con mensaje de error
3. Si pasa las dos → ejecuta la vista

---

# PARTE 4 — Las URLs

## ¿Cómo funcionan las URLs en Django?

Django tiene un archivo de URLs que actúa como un mapa:
"Si alguien pide esta dirección, llama a esta vista".

**config/urls.py** (el mapa principal):

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),          # URLs de la página de inicio
    path('cursos/', include('cursos.urls')), # URLs de cursos
    path('matriculas/', include('matriculas.urls')),
    path('profesores/', include('profesores.urls')),
]
```

**cursos/urls.py** (el mapa de cursos):

```python
urlpatterns = [
    path('', ListaCursosView.as_view(), name='lista_cursos'),
    path('nuevo/', CursoCreateView.as_view(), name='curso_crear'),
    path('<slug:slug>/', CursoDetailView.as_view(), name='detalle_curso'),
    path('<slug:slug>/editar/', CursoUpdateView.as_view(), name='curso_editar'),
    path('<slug:slug>/eliminar/', CursoDeleteView.as_view(), name='curso_eliminar'),
]
```

`<slug:slug>` es un **parámetro de URL**: captura lo que haya en esa
posición y lo pasa a la vista. Si alguien va a `/cursos/python-basico/`,
Django captura `python-basico` y lo pasa como `slug`.

**El parámetro `name`:** cada URL tiene un nombre. Esto es muy importante
porque permite referenciarla desde las plantillas sin escribir la URL
completa:

```html
<!-- En lugar de escribir esto (si la URL cambia, hay que cambiar todo) -->
<a href="/cursos/nuevo/">Nuevo curso</a>

<!-- Escribimos esto (Django calcula la URL automáticamente) -->
<a href="{% url 'curso_crear' %}">Nuevo curso</a>
```

---

# PARTE 5 — Las plantillas

## ¿Qué es una plantilla?

Una plantilla es un archivo HTML con etiquetas especiales de Django que
permiten mostrar datos dinámicos.

**Variables:** `{{ variable }}`
```html
<h1>{{ curso.nombre }}</h1>
<!-- Si curso.nombre es "Python Básico", muestra: -->
<h1>Python Básico</h1>
```

**Etiquetas:** `{% etiqueta %}`
```html
{% if user.is_authenticated %}
    <p>Bienvenido, {{ user.username }}</p>
{% else %}
    <p>Por favor, inicia sesión</p>
{% endif %}
```

**Bucles:**
```html
{% for curso in cursos %}
    <p>{{ curso.nombre }}</p>
{% empty %}
    <p>No hay cursos disponibles</p>
{% endfor %}
```

`{% empty %}` se ejecuta si la lista está vacía.

**Herencia de plantillas:**

Tenemos una plantilla base (`base.html`) con la estructura común
(menú, cabecera, pie de página). Las demás plantillas la "extienden":

```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head><title>{% block title %}Gestión Formación{% endblock %}</title></head>
<body>
    <nav>... menú ...</nav>
    {% block content %}{% endblock %}
</body>
</html>
```

```html
<!-- lista_cursos.html -->
{% extends 'base.html' %}

{% block title %}Cursos{% endblock %}

{% block content %}
    <h1>Listado de cursos</h1>
    ... contenido específico de esta página ...
{% endblock %}
```

Esto evita repetir el menú y la estructura en cada página.

---

# PARTE 6 — Capítulo a Capítulo

---

## CAPÍTULO 6 — Sistema de Matrículas

### ¿Qué hicimos?

Antes del capítulo 6, los usuarios podían ver cursos pero no
matricularse en ellos. En este capítulo añadimos todo el sistema
de matriculación.

### El modelo Matricula

Ya explicado arriba. La clave es `unique_together`:

```python
class Meta:
    unique_together = ('alumno', 'curso')
```

Esto funciona a nivel de base de datos, no solo en Python.
Aunque alguien intente saltarse la web y meter datos directamente
en la base de datos, no podrá crear una matrícula duplicada.

### La vista matricularse

```python
@login_required
def matricularse(request, curso_id):
    # 1. Busca el curso (si no existe o no está activo → error 404)
    curso = get_object_or_404(Curso, pk=curso_id, activo=True)

    # 2. Solo los alumnos pueden matricularse
    if request.user.tipo != 'alumno':
        messages.error(request, "Sólo los alumnos pueden matricularse.")
        return redirect('detalle_curso', curso.slug)

    # 3. Comprueba si quedan plazas
    inscritos = curso.matriculas.count()
    if inscritos >= curso.plazas:
        messages.error(request, "No quedan plazas.")
        return redirect('detalle_curso', curso.slug)

    # 4. Intenta matricular (o detecta que ya estaba matriculado)
    matricula, creada = Matricula.objects.get_or_create(
        alumno=request.user,
        curso=curso
    )

    # 5. Muestra mensaje según el resultado
    if creada:
        messages.success(request, "Matrícula realizada correctamente.")
    else:
        messages.warning(request, "Ya estás matriculado en este curso.")

    # 6. Redirige de vuelta al curso
    return redirect('detalle_curso', curso.slug)
```

**¿Por qué `get_or_create`?**
En lugar de comprobar primero si existe y luego crear, lo hace en una
sola operación. Devuelve una tupla:
- `matricula`: el objeto (existente o nuevo)
- `creada`: `True` si se acaba de crear, `False` si ya existía

### El sistema de mensajes

Django tiene un sistema de notificaciones temporales que solo aparecen
una vez y luego desaparecen:

```python
messages.success(request, "Operación realizada")  # Verde
messages.error(request, "Ha ocurrido un error")   # Rojo
messages.warning(request, "Atención")             # Amarillo
messages.info(request, "Información")             # Azul
```

En la plantilla:
```html
{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">{{ message }}</div>
    {% endfor %}
{% endif %}
```

`message.tags` devuelve `success`, `error`, `warning` o `info`, que
coincide exactamente con las clases de Bootstrap (`alert-success`, etc.).

### La vista mis_cursos

```python
@login_required
def mis_cursos(request):
    matriculas = Matricula.objects.filter(
        alumno=request.user
    ).select_related('curso', 'curso__profesor', 'curso__profesor__usuario')
    return render(request, 'matriculas/mis_cursos.html', {'matriculas': matriculas})
```

**select_related()**: cuando Django consulta las matrículas, normalmente
haría una consulta extra por cada curso para obtener el nombre del profesor.
Con `select_related()` hace todo en una sola consulta usando JOIN en SQL.

El `__` (doble guion bajo) navega relaciones:
- `'curso'`: trae el curso de cada matrícula
- `'curso__profesor'`: trae el profesor de ese curso
- `'curso__profesor__usuario'`: trae el usuario de ese profesor

Sin `select_related`, 10 matrículas = 31 consultas SQL.
Con `select_related`, 10 matrículas = 1 consulta SQL.

---

## CAPÍTULO 7 — Dashboard del Alumno y Cancelación

### El Dashboard

```python
@login_required
def dashboard(request):
    # Cuenta total de matrículas del usuario
    total_matriculas = Matricula.objects.filter(alumno=request.user).count()

    # Última matrícula (la más reciente)
    ultima_matricula = (
        Matricula.objects.filter(alumno=request.user)
        .select_related('curso')
        .order_by('-fecha_matricula')  # El - invierte: más reciente primero
        .first()                       # Solo el primero
    )

    # Próximo curso (el que empieza antes)
    proximo_curso = (
        Curso.objects.filter(matriculas__alumno=request.user)
        .order_by('fecha_inicio')
        .first()
    )

    # Últimas 5 matrículas
    ultimas_matriculas = (
        Matricula.objects.filter(alumno=request.user)
        .select_related('curso')
        .order_by('-fecha_matricula')[:5]  # [:5] = solo los 5 primeros
    )

    # Cursos disponibles en la plataforma
    cursos_disponibles = Curso.objects.filter(activo=True).count()
```

**La notación `matriculas__alumno`:**

`Curso.objects.filter(matriculas__alumno=request.user)` significa:
"Dame los cursos cuyas matrículas tienen como alumno al usuario actual".

Django navega automáticamente de Curso → Matricula → Usuario usando
los `related_name` que definimos en los modelos.

**[:5]** es un "slice" (trozo) de Python. Como cuando cortas una lista:
```python
lista = [1, 2, 3, 4, 5, 6, 7]
lista[:3]  # [1, 2, 3] — los 3 primeros
lista[2:5] # [3, 4, 5] — del índice 2 al 4
```

### Cancelar matrícula

```python
@login_required
def cancelar_matricula(request, matricula_id):
    # Busca la matrícula que sea del usuario actual
    matricula = get_object_or_404(Matricula, pk=matricula_id, alumno=request.user)
    matricula.delete()
    messages.success(request, 'Matrícula cancelada.')
    return redirect('mis_cursos')
```

**Seguridad importante:** el filtro `alumno=request.user` impide que
un usuario cancele la matrícula de otro. Si no lo pusiéramos, un usuario
malicioso podría ir a `/matriculas/cancelar/1/` y cancelar la matrícula
del alumno con ID 1, aunque no fuera la suya.

### Menú inteligente

En `base.html` mostramos opciones diferentes según el tipo de usuario:

```html
{% if user.is_authenticated %}
    {% if user.tipo == 'alumno' %}
        <a href="{% url 'dashboard' %}">Dashboard</a>
        <a href="{% url 'mis_cursos' %}">Mis Cursos</a>
    {% endif %}
    {% if user.tipo == 'profesor' %}
        <a href="{% url 'dashboard_profesor' %}">Panel Profesor</a>
        <a href="{% url 'mis_cursos_profesor' %}">Mis Cursos</a>
    {% endif %}
{% else %}
    <a href="{% url 'login' %}">Login</a>
{% endif %}
```

---

## CAPÍTULO 8 — Búsquedas, Filtros, Paginación y Slugs

### ¿Qué es un Slug?

Un slug es una versión "amigable para URLs" de un texto.

Antes: `/cursos/1/` — No dice nada sobre qué es el curso.
Después: `/cursos/python-basico/` — Descriptivo y mejor para buscadores.

Esto mejora el **SEO** (Search Engine Optimization), es decir, cómo
te encuentra Google. Las URLs descriptivas posicionan mejor.

**¿Cómo se genera automáticamente?**

```python
from django.utils.text import slugify

slugify("Python Básico")          # → "python-basico"
slugify("Django para todos!!!")   # → "django-para-todos"
slugify("¿Qué es Docker?")       # → "que-es-docker"
```

En el modelo, lo generamos automáticamente al guardar:

```python
def save(self, *args, **kwargs):
    if not self.slug:           # Solo si no tiene slug ya
        self.slug = slugify(self.nombre)
    super().save(*args, **kwargs)
```

### Búsqueda con Q objects

Para buscar en varios campos a la vez usamos `Q`:

```python
from django.db.models import Q

cursos = Curso.objects.filter(
    Q(nombre__icontains=busqueda) | Q(descripcion__icontains=busqueda)
)
```

`Q` permite combinar condiciones:
- `|` significa OR (o esto, o aquello)
- `&` significa AND (esto Y aquello)
- `~` significa NOT (que no sea esto)

`icontains` = "contains" (contiene) + "i" de "insensitive" (sin distinguir
mayúsculas). Busca "python" y encuentra "Python", "PYTHON", "python", etc.

### Paginación

```python
from django.core.paginator import Paginator

# 1. Crear el paginador con 6 elementos por página
paginator = Paginator(cursos, 6)

# 2. Saber qué página pide el usuario (viene en la URL como ?page=2)
page_number = request.GET.get('page')

# 3. Obtener solo los cursos de esa página
cursos = paginator.get_page(page_number)
```

En la plantilla, `page_obj` tiene información sobre la paginación:

```html
{% if page_obj.has_previous %}
    <a href="?page={{ page_obj.previous_page_number }}">Anterior</a>
{% endif %}

Página {{ page_obj.number }} de {{ paginator.num_pages }}

{% if page_obj.has_next %}
    <a href="?page={{ page_obj.next_page_number }}">Siguiente</a>
{% endif %}
```

### Parámetros GET

Cuando buscas en un formulario, los datos viajan en la URL:
`/cursos/?buscar=python&profesor=3&page=2`

En la vista se leen con `request.GET.get()`:

```python
busqueda = request.GET.get('buscar', '')    # '' es el valor por defecto
profesor_id = request.GET.get('profesor', '')
```

Si el usuario no puso nada en el buscador, `busqueda` será `''` (vacío).

### Data Migration

Cuando añadimos el campo `slug` a los cursos que ya existían en la base
de datos, esos cursos tenían el slug vacío. Una **data migration** es una
migración que no solo cambia la estructura de la tabla, sino que también
modifica los datos:

```python
def poblar_slugs(apps, schema_editor):
    Curso = apps.get_model('cursos', 'Curso')
    for curso in Curso.objects.all():
        curso.slug = slugify(curso.nombre)
        curso.save()
```

Esta función se ejecuta una sola vez al hacer `migrate`, y genera
automáticamente el slug de todos los cursos existentes.

---

## CAPÍTULO 9 — Panel del Profesor y Permisos

### Autenticación vs Autorización

Son conceptos diferentes y muy importantes:

**Autenticación**: comprobar *quién eres*.
- ¿Tienes cuenta? ¿La contraseña es correcta?
- En Django: `@login_required`, `request.user.is_authenticated`

**Autorización**: comprobar *qué puedes hacer*.
- ¿Tienes permiso para esta acción?
- En Django: decoradores personalizados, `UserPassesTestMixin`

Ejemplo de la vida real:
- Entrar a un edificio con tu tarjeta → **Autenticación**
- Poder entrar solo a ciertas plantas → **Autorización**

### Decorador profesor_required

```python
def profesor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.tipo != 'profesor':
            messages.error(request, 'Acceso denegado.')
            return redirect('inicio')
        return view_func(request, *args, **kwargs)
    return wrapper
```

¿Cómo funciona un decorador? Es una función que recibe otra función
y devuelve una versión "mejorada" de esa función:

```
profesor_required(vista_original) → nueva_vista_con_comprobaciones
```

Cuando ponemos `@profesor_required` encima de una vista, Python ejecuta
automáticamente `profesor_required(vista)` y sustituye la vista por
el resultado.

### annotate() y Count()

```python
from django.db.models import Count

cursos = (
    Curso.objects.filter(profesor=request.user.profesor)
    .annotate(total_alumnos=Count('matriculas'))
)
```

`annotate()` añade un campo calculado a cada objeto. Es como añadir
una columna extra en los resultados de la consulta.

Sin `annotate`, para saber cuántos alumnos tiene cada curso tendrías
que hacer una consulta por cada curso (N consultas).

Con `annotate`, Django lo calcula todo en una sola consulta SQL.

Después puedes usar `curso.total_alumnos` en Python y en la plantilla:

```html
{% for curso in cursos %}
    {{ curso.nombre }} — {{ curso.total_alumnos }} alumnos
{% endfor %}
```

### Acceder al perfil del profesor

```python
profesor = request.user.profesor
```

Esto funciona gracias al `related_name='profesor'` que pusimos en el
modelo `Profesor`. Django crea automáticamente ese acceso inverso.

---

## CAPÍTULO 10 — Class Based Views (CBV)

### ¿Por qué CBV?

Imagina que tienes 10 apps cada una con listados, detalles, formularios...
Con FBV escribes la misma lógica 10 veces. Con CBV, Django ya tiene
esa lógica y solo tienes que configurar qué modelo usar.

### ListView

Muestra una lista de objetos:

```python
class ListaCursosView(ListView):
    model = Curso                               # Qué modelo usar
    template_name = 'cursos/lista_cursos.html' # Qué plantilla usar
    context_object_name = 'cursos'             # Nombre en la plantilla
    paginate_by = 6                            # Paginación automática

    def get_queryset(self):
        # Personaliza la consulta (aquí añadimos búsqueda y filtros)
        queryset = Curso.objects.filter(activo=True)
        busqueda = self.request.GET.get('buscar', '')
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        return queryset

    def get_context_data(self, **kwargs):
        # Añade variables extra a la plantilla
        context = super().get_context_data(**kwargs)
        context['profesores'] = Profesor.objects.all()
        return context
```

Nota: en CBV, `request` se accede como `self.request` (con `self.`).

### DetailView

Muestra el detalle de un único objeto:

```python
class CursoDetailView(DetailView):
    model = Curso
    template_name = 'cursos/detalle_curso.html'
    context_object_name = 'curso'
    slug_field = 'slug'       # Qué campo del modelo usar para buscar
    slug_url_kwarg = 'slug'   # Qué parámetro de la URL usar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ocupadas'] = self.object.matriculas.count()
        return context
```

`self.object` es el objeto encontrado automáticamente por Django.

### CreateView

Muestra un formulario y guarda el nuevo objeto:

```python
class CursoCreateView(LoginRequiredMixin, ProfesorMixin, CreateView):
    model = Curso
    form_class = CursoForm                  # Formulario personalizado
    template_name = 'cursos/curso_form.html'
    success_url = reverse_lazy('lista_cursos')  # A dónde ir tras guardar
```

### UpdateView y DeleteView

```python
class CursoUpdateView(LoginRequiredMixin, ProfesorMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/curso_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('lista_cursos')

class CursoDeleteView(LoginRequiredMixin, ProfesorMixin, DeleteView):
    model = Curso
    template_name = 'cursos/curso_confirm_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('lista_cursos')
```

### Mixins

Un Mixin es una clase que añade comportamiento extra a una CBV.
Se ponen antes de la vista genérica en la lista de herencia:

```python
class CursoCreateView(LoginRequiredMixin, ProfesorMixin, CreateView):
```

Django los procesa de izquierda a derecha:
1. `LoginRequiredMixin` — ¿Está autenticado?
2. `ProfesorMixin` — ¿Es profesor?
3. `CreateView` — Si pasa los dos, muestra el formulario

**LoginRequiredMixin**: equivalente a `@login_required` para CBV.

**ProfesorMixin**:
```python
class ProfesorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.tipo == 'profesor'
```

`UserPassesTestMixin` ejecuta `test_func()`. Si devuelve `False`, deniega
el acceso (muestra error 403).

### ModelForm con Bootstrap

```python
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'profesor', 'fecha_inicio',
                  'fecha_fin', 'plazas', 'activo', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
```

`ModelForm` genera automáticamente el formulario HTML a partir del modelo.
Solo tienes que decirle qué campos incluir y cómo renderizarlos.

`widgets` personaliza cómo aparece cada campo:
- `class: 'form-control'` aplica el estilo de Bootstrap
- `type: 'date'` muestra el selector de fecha del navegador

### reverse_lazy() vs reverse()

`reverse('lista_cursos')` calcula la URL de `lista_cursos`.
Se usa en funciones porque se ejecuta cuando se llama.

`reverse_lazy('lista_cursos')` hace lo mismo pero "perezosamente":
no calcula la URL hasta que se necesita. Se usa en clases porque
el atributo `success_url` se evalúa cuando se define la clase,
antes de que Django haya cargado todas las URLs.

### as_view()

Para registrar una CBV en las URLs, hay que llamar a `.as_view()`:

```python
path('', ListaCursosView.as_view(), name='lista_cursos'),
```

`as_view()` convierte la clase en una función que Django puede llamar.
Esto es necesario porque Django espera funciones en las URLs, no clases.

---

# PARTE 7 — El Panel de Administración

Django incluye un panel de administración automático en `/admin/`.
Nosotros lo personalizamos con Jazzmin (tema) y configuraciones extra.

## Registrar un modelo en el admin

```python
from django.contrib import admin
from .models import Matricula

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'curso', 'fecha_matricula')  # Columnas visibles
    search_fields = ('alumno__username', 'curso__nombre')  # Búsqueda
    ordering = ('-fecha_matricula',)                       # Orden por defecto
    list_filter = ('curso', 'fecha_matricula')             # Filtros laterales
    date_hierarchy = 'fecha_matricula'                     # Navegación por fecha
    readonly_fields = ('fecha_matricula',)                 # Campo no editable
```

`@admin.register(Matricula)` conecta el modelo con la configuración del admin.

## Campos calculados en el admin

```python
def alumnos(self, obj):
    return obj.matriculas.count()
alumnos.short_description = 'Alumnos'  # Nombre de la columna

list_display = ('nombre', 'alumnos', 'activo')
```

## list_editable

```python
list_editable = ('activo',)
```

Permite editar ese campo directamente desde el listado sin entrar
en el detalle de cada objeto. Muy útil para activar/desactivar cursos.

## prepopulated_fields

```python
prepopulated_fields = {'slug': ('nombre',)}
```

En el formulario del admin, cuando escribes el nombre del curso,
el campo slug se rellena automáticamente con JavaScript.

---

# PARTE 8 — Flujo completo de la aplicación

## ¿Qué puede hacer cada usuario?

### Usuario NO registrado (anónimo)
- Ver el catálogo de cursos
- Buscar y filtrar cursos
- Ver el detalle de un curso
- Registrarse
- Iniciar sesión

### Usuario registrado como ALUMNO
- Todo lo anterior
- Matricularse en cursos (si hay plazas)
- Ver "Mis Cursos" — lista de cursos matriculados
- Cancelar matrículas
- Ver su Dashboard con estadísticas personales

### Usuario registrado como PROFESOR
- Ver el catálogo (igual que todos)
- Ver "Panel Profesor" con estadísticas
- Ver sus cursos y cuántos alumnos tiene cada uno
- Crear nuevos cursos
- Editar sus cursos
- Eliminar sus cursos

### Superusuario (administrador)
- Acceder a `/admin/`
- Gestionar todos los usuarios, profesores, cursos y matrículas
- Activar/desactivar cursos desde el listado

---

# PARTE 9 — Glosario completo

| Término | Significado |
|---|---|
| **Python** | Lenguaje de programación que usamos |
| **Django** | Framework web en Python |
| **Framework** | Conjunto de herramientas ya construidas para un tipo de proyecto |
| **Base de datos** | Sistema para guardar información de forma permanente |
| **PostgreSQL** | El sistema de base de datos que usamos |
| **SQL** | Lenguaje para hablar con bases de datos |
| **ORM** | Sistema que traduce Python a SQL automáticamente |
| **Modelo** | Clase Python que representa una tabla en la base de datos |
| **Migración** | Archivo que aplica cambios del modelo a la base de datos |
| **Vista** | Función o clase que procesa peticiones y devuelve respuestas |
| **Plantilla** | Archivo HTML con etiquetas especiales de Django |
| **URL** | Dirección web. En Django, mapea rutas a vistas |
| **FBV** | Function Based View — vista como función |
| **CBV** | Class Based View — vista como clase |
| **ListView** | CBV para listar objetos |
| **DetailView** | CBV para ver el detalle de un objeto |
| **CreateView** | CBV para crear objetos con formulario |
| **UpdateView** | CBV para editar objetos con formulario |
| **DeleteView** | CBV para eliminar objetos con confirmación |
| **Mixin** | Clase que añade comportamiento a una CBV |
| **Decorador** | Función que añade comportamiento a otra función |
| **@login_required** | Decorador que exige que el usuario esté autenticado |
| **LoginRequiredMixin** | Lo mismo pero para CBV |
| **UserPassesTestMixin** | CBV Mixin que comprueba una condición personalizada |
| **Autenticación** | Verificar quién eres (login) |
| **Autorización** | Verificar qué puedes hacer (permisos) |
| **ForeignKey** | Relación N:1 entre dos modelos |
| **OneToOneField** | Relación 1:1 entre dos modelos |
| **ManyToManyField** | Relación N:M entre dos modelos |
| **Tabla intermedia** | Tabla que implementa una relación N:M con datos extra |
| **unique_together** | Restricción que impide duplicados en combinación de campos |
| **related_name** | Nombre para acceder a la relación inversa |
| **select_related** | Optimiza consultas FK con JOIN |
| **prefetch_related** | Optimiza consultas inversas/M2M |
| **annotate** | Añade campos calculados a un queryset |
| **Count** | Función de aggregación para contar |
| **Q object** | Permite condiciones OR/AND en consultas ORM |
| **icontains** | Búsqueda de texto sin distinguir mayúsculas |
| **Slug** | Texto amigable para URLs (sin espacios ni símbolos) |
| **slugify** | Función que convierte texto a slug |
| **db_index** | Índice en la base de datos para búsquedas más rápidas |
| **Paginator** | Divide un queryset en páginas |
| **request.GET** | Datos que viajan en la URL (?param=valor) |
| **request.POST** | Datos que viajan en formularios enviados |
| **render()** | Combina plantilla con datos y devuelve HTML |
| **redirect()** | Redirige al navegador a otra URL |
| **get_object_or_404** | Busca un objeto y devuelve error 404 si no existe |
| **get_or_create** | Busca un objeto; si no existe, lo crea |
| **messages** | Sistema de notificaciones temporales de Django |
| **ModelForm** | Formulario generado automáticamente desde un modelo |
| **Widget** | Elemento HTML que representa un campo del formulario |
| **reverse** | Calcula la URL de un nombre de URL |
| **reverse_lazy** | Lo mismo pero se evalúa más tarde (para clases) |
| **as_view()** | Convierte una CBV en función para registrar en URLs |
| **AbstractUser** | Modelo de usuario base de Django que se puede extender |
| **AUTH_USER_MODEL** | Configuración que indica cuál es el modelo de usuario |
| **SEO** | Optimización para buscadores (Google, etc.) |
| **Jazzmin** | Tema visual para el panel de administración de Django |
| **Bootstrap** | Librería CSS para diseño visual |
| **venv** | Entorno virtual de Python |
| **.env** | Archivo con variables de entorno secretas |
| **requirements.txt** | Lista de librerías necesarias para el proyecto |
| **Git** | Sistema de control de versiones |
| **GitHub** | Plataforma para alojar repositorios Git |
| **commit** | Foto guardada del estado del proyecto |
| **push** | Subir commits al repositorio remoto (GitHub) |

---

# PARTE 10 — Comandos que hemos usado

```bash
# Arrancar el servidor de desarrollo
python manage.py runserver
# Abrir en: http://127.0.0.1:8000/

# Crear migraciones (tras cambiar un modelo)
python manage.py makemigrations

# Aplicar migraciones a la base de datos
python manage.py migrate

# Ver el estado de las migraciones
python manage.py showmigrations

# Crear superusuario para el admin
python manage.py createsuperuser

# Verificar que el proyecto no tiene errores de configuración
python manage.py check

# Abrir la consola de Django (para probar consultas)
python manage.py shell

# Ver el SQL generado por una migración
python manage.py sqlmigrate cursos 0001

# Git: guardar cambios
git add nombre_archivo.py
git commit -m "Descripción del cambio"
git push

# Git: ver el historial
git log --oneline
```

---

# PARTE 11 — Estructura de archivos final

```
gestion_formacion/
│
├── config/
│   ├── settings.py     ← Configuración global
│   ├── urls.py         ← URLs principales
│   └── wsgi.py         ← Punto de entrada del servidor
│
├── core/
│   ├── views.py        ← Vista: página de inicio
│   └── urls.py         ← URL: /
│
├── usuarios/
│   ├── models.py       ← Modelo: Usuario (AbstractUser + tipo)
│   ├── views.py        ← Vista: registro
│   ├── forms.py        ← Formulario: registro
│   ├── decorators.py   ← Decorador: @profesor_required
│   ├── urls.py         ← URL: /usuarios/registro/
│   └── admin.py        ← Admin: gestión de usuarios
│
├── profesores/
│   ├── models.py       ← Modelo: Profesor
│   ├── views.py        ← Vistas: dashboard_profesor, mis_cursos_profesor
│   ├── urls.py         ← URLs: /profesores/dashboard/, /profesores/mis-cursos/
│   └── admin.py        ← Admin: gestión de profesores
│
├── cursos/
│   ├── models.py       ← Modelo: Curso (con slug, db_index)
│   ├── views.py        ← Vistas CBV: Lista, Detalle, Crear, Editar, Eliminar
│   ├── forms.py        ← Formulario: CursoForm con widgets Bootstrap
│   ├── urls.py         ← URLs: /cursos/, /cursos/<slug>/, /cursos/nuevo/...
│   └── admin.py        ← Admin: filtros, miniatura, list_editable
│
├── matriculas/
│   ├── models.py       ← Modelo: Matricula (tabla intermedia N:M)
│   ├── views.py        ← Vistas: matricularse, cancelar, mis_cursos, dashboard
│   ├── urls.py         ← URLs: /matriculas/...
│   └── admin.py        ← Admin: gestión de matrículas
│
└── templates/
    ├── base.html                        ← Plantilla base (menú, mensajes)
    ├── core/
    │   └── inicio.html                  ← Página de inicio
    ├── cursos/
    │   ├── lista_cursos.html            ← Catálogo con búsqueda y filtros
    │   ├── detalle_curso.html           ← Detalle de un curso
    │   ├── curso_form.html              ← Formulario crear/editar
    │   └── curso_confirm_delete.html    ← Confirmación de borrado
    ├── matriculas/
    │   ├── dashboard.html               ← Dashboard del alumno
    │   └── mis_cursos.html              ← Cursos matriculados
    ├── profesores/
    │   ├── dashboard.html               ← Panel del profesor
    │   └── mis_cursos.html              ← Cursos del profesor
    └── registration/
        └── login.html                   ← Página de login
```
