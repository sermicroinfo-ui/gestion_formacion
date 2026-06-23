from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q
from profesores.models import Profesor
from .models import Curso
from .forms import CursoForm


class ProfesorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.tipo == 'profesor'


class ListaCursosView(ListView):
    model = Curso
    template_name = 'cursos/lista_cursos.html'
    context_object_name = 'cursos'
    paginate_by = 6

    def get_queryset(self):
        queryset = Curso.objects.filter(activo=True).select_related(
            'profesor', 'profesor__usuario'
        ).order_by('fecha_inicio')
        busqueda = self.request.GET.get('buscar', '')
        profesor_id = self.request.GET.get('profesor', '')
        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda) | Q(descripcion__icontains=busqueda)
            )
        if profesor_id:
            queryset = queryset.filter(profesor_id=profesor_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_cursos'] = self.object_list.count()
        context['profesores'] = Profesor.objects.all()
        return context


class CursoDetailView(DetailView):
    model = Curso
    template_name = 'cursos/detalle_curso.html'
    context_object_name = 'curso'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Curso.objects.filter(activo=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ocupadas'] = self.object.matriculas.count()
        return context


class CursoCreateView(LoginRequiredMixin, ProfesorMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/curso_form.html'
    success_url = reverse_lazy('lista_cursos')


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
