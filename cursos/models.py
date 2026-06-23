from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from profesores.models import Profesor


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
    imagen = models.ImageField(
        upload_to='cursos/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def clean(self):
        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_fin < self.fecha_inicio:
                raise ValidationError(
                    "La fecha final no puede ser anterior a la inicial"
                )
