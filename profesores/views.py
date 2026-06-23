from django.shortcuts import render
from django.db.models import Count
from cursos.models import Curso
from matriculas.models import Matricula
from usuarios.decorators import profesor_required


@profesor_required
def dashboard_profesor(request):
    profesor = request.user.profesor
    cursos = Curso.objects.filter(profesor=profesor)
    total_cursos = cursos.count()
    total_alumnos = Matricula.objects.filter(curso__profesor=profesor).count()
    curso_popular = (
        Curso.objects.filter(profesor=profesor)
        .annotate(total=Count('matriculas'))
        .order_by('-total')
        .first()
    )
    return render(request, 'profesores/dashboard.html', {
        'total_cursos': total_cursos,
        'total_alumnos': total_alumnos,
        'curso_popular': curso_popular,
    })


@profesor_required
def mis_cursos_profesor(request):
    cursos = (
        Curso.objects.filter(profesor=request.user.profesor)
        .annotate(total_alumnos=Count('matriculas'))
    )
    return render(request, 'profesores/mis_cursos.html', {'cursos': cursos})
