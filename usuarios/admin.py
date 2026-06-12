from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('tipo',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Adicional', {'fields': ('tipo',)}),
    )
    list_display = ('username', 'email', 'tipo', 'is_staff', 'is_active')

admin.site.register(Usuario, UsuarioAdmin)