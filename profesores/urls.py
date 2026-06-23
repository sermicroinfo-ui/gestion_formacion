from django.urls import path
from .views import dashboard_profesor, mis_cursos_profesor

urlpatterns = [
    path('dashboard/', dashboard_profesor, name='dashboard_profesor'),
    path('mis-cursos/', mis_cursos_profesor, name='mis_cursos_profesor'),
]
