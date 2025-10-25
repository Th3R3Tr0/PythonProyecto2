from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import ProfesorFormulario, ProfesorForm
from django.db import models

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
    query = request.GET.get('q')  # Captura lo que se escribe en el buscador
    if query:
        profesores = Profesor.objects.filter(
            models.Q(nombre__icontains=query) |
            models.Q(apellido__icontains=query) |
            models.Q(profesion__icontains=query)
        )
    else:
        profesores = Profesor.objects.all()


    return render(request, 'myapp/profesores.html', {
        'profesores': profesores,
        'query': query,
    })



def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'myapp/entregables.html',{'entregables': entregables})

def profesorFormulario(request):
    if request.method == 'POST':
        form = ProfesorFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            profesion = form.cleaned_data['profesion']
            profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profesor.save()
            return redirect('myapp:profesores')  # Redirige a la lista de profesores
    else:
         form = ProfesorFormulario()
    return render(request, 'myapp/profesor_formulario.html', {'form': form})

def profesor_editar(request, id):
    profesor = get_object_or_404(Profesor, id=id)
   
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('myapp:profesores')
    else:
        form = ProfesorForm(instance=profesor)
   
    return render(request, 'myapp/profesor_editar.html', {'form': form, 'profesor': profesor})

def profesor_eliminar(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    profesor.delete()
    return redirect('myapp:profesores')  # vuelve a la lista de profesores