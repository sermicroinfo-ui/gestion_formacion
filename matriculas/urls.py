from django.urls import path
from .views import matricularse, mis_cursos, cancelar_matricula, dashboard

urlpatterns = [
    path('matricular/<int:curso_id>/', matricularse, name='matricularse'),
    path('mis-cursos/', mis_cursos, name='mis_cursos'),
    path('cancelar/<int:matricula_id>/', cancelar_matricula, name='cancelar_matricula'),
    path('dashboard/', dashboard, name='dashboard'),
]
