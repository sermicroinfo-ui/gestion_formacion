from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from datetime import timedelta
from .models import Curso

class FiltroEstado(admin.SimpleListFilter):
    title = 'estado del curso'
    parameter_name = 'activo'

    def lookups(self, request, model_admin):
        return [
            ('1', 'Publicado'),
            ('0', 'Oculto'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(activo=True)
        if self.value() == '0':
            return queryset.filter(activo=False)

class FiltroFecha(admin.SimpleListFilter):
    title = 'fecha'
    parameter_name = 'filtro_fecha'

    def lookups(self, request, model_admin):
        return [
            ('hoy', 'Empieza hoy'),
            ('en_curso', 'En curso ahora'),
            ('proximos_7', 'Próximos 7 días'),
            ('pasados_7', 'Últimos 7 días'),
            ('este_mes', 'Este mes'),
            ('proximo_mes', 'Próximo mes'),
        ]

    def queryset(self, request, queryset):
        hoy = timezone.now().date()
        if self.value() == 'hoy':
            return queryset.filter(fecha_inicio=hoy)
        if self.value() == 'en_curso':
            return queryset.filter(
                fecha_inicio__lte=hoy,
                fecha_fin__gte=hoy
            )
        if self.value() == 'proximos_7':
            return queryset.filter(
                fecha_inicio__gte=hoy,
                fecha_inicio__lte=hoy + timedelta(days=7)
            )
        if self.value() == 'pasados_7':
            return queryset.filter(
                fecha_inicio__gte=hoy - timedelta(days=7),
                fecha_inicio__lte=hoy
            )
        if self.value() == 'este_mes':
            return queryset.filter(
                fecha_inicio__year=hoy.year,
                fecha_inicio__month=hoy.month
            )
        if self.value() == 'proximo_mes':
            if hoy.month == 12:
                return queryset.filter(
                    fecha_inicio__year=hoy.year + 1,
                    fecha_inicio__month=1
                )
            return queryset.filter(
                fecha_inicio__year=hoy.year,
                fecha_inicio__month=hoy.month + 1
            )


class FiltroMes(admin.SimpleListFilter):
    title = 'mes'
    parameter_name = 'mes'

    def lookups(self, request, model_admin):
        return [
            ('1', 'Enero'), ('2', 'Febrero'), ('3', 'Marzo'),
            ('4', 'Abril'), ('5', 'Mayo'), ('6', 'Junio'),
            ('7', 'Julio'), ('8', 'Agosto'), ('9', 'Septiembre'),
            ('10', 'Octubre'), ('11', 'Noviembre'), ('12', 'Diciembre'),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(fecha_inicio__month=self.value())


class FiltroAnio(admin.SimpleListFilter):
    title = 'año'
    parameter_name = 'anio'

    def lookups(self, request, model_admin):
        return [(str(a), str(a)) for a in range(2024, 2031)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(fecha_inicio__year=self.value())


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'miniatura',
        'nombre',
        'profesor',
        'fecha_inicio',
        'fecha_fin',
        'activo',
    )
    search_fields = (
        'nombre',
        'descripcion',
        'profesor__usuario__first_name',
        'profesor__usuario__last_name',
    )
    list_filter = (FiltroEstado, FiltroFecha, FiltroMes, FiltroAnio,)
    ordering = ('nombre',)
    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'descripcion', 'profesor',)
        }),
        ('Planificación', {
            'fields': ('fecha_inicio', 'fecha_fin', 'plazas',)
        }),
        ('Publicación', {
            'fields': ('activo', 'imagen',)
        }),
    )

    def miniatura(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" width="80"/>',
                obj.imagen.url
            )
        return '-'

    miniatura.short_description = "Imagen"