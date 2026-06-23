from django.urls import path
from .views import (
    ListaCursosView,
    CursoDetailView,
    CursoCreateView,
    CursoUpdateView,
    CursoDeleteView,
)

urlpatterns = [
    path('', ListaCursosView.as_view(), name='lista_cursos'),
    path('nuevo/', CursoCreateView.as_view(), name='curso_crear'),
    path('<slug:slug>/', CursoDetailView.as_view(), name='detalle_curso'),
    path('<slug:slug>/editar/', CursoUpdateView.as_view(), name='curso_editar'),
    path('<slug:slug>/eliminar/', CursoDeleteView.as_view(), name='curso_eliminar'),
]
