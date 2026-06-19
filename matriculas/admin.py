from django.contrib import admin
from .models import Matricula


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'curso', 'fecha_matricula')
    search_fields = ('alumno__username', 'curso__nombre')
    ordering = ('-fecha_matricula',)
    list_filter = ('curso', 'fecha_matricula')
    date_hierarchy = 'fecha_matricula'
    readonly_fields = ('fecha_matricula',)
