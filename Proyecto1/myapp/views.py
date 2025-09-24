from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable
# Create your views here.


def index(request):
    return render(request, "myapp/index.html")

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myApp/estudiantes_list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'myApp/estudiante_detail.html', {'estudiante': estudiante})

def index(request):
    context = {"mensaje":"Bienvenidos a mi aplicación Django"}
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/index.html', context)


def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/estudiantes_list.html', {'estudiantes': estudiantes})


def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'myapp/cursos.html',{'cursos': cursos})


def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'myapp/profesores.html', {'profesores': profesores})


def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'myapp/entregables.html',{'entregables': entregables})