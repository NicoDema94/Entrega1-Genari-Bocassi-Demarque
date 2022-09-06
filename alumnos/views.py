from typing import Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from alumnos.models import Alumnos, Curso, Ubicacion
from alumnos.forms import CursoFormulario, CursoFormulario1, CursoFormulario2

def inicio(request):

      return render(request, "Alumnos/inicio.html")

def ubicacion(request):
      ubicacion = Ubicacion.objects.all()
      return render(request, "Alumnos/ubicacion.html")

def curso(request):
      curso = Curso.objects.all()
      return render(request, "Alumnos/curso.html", {'cursos': curso})

def estudiantes(request):

      return render(request, "Alumnos/estudiantes.html")

def curso_formulario(request):
      if request.method == 'POST':
            data_formulario: Dict = request.POST
            curso = Curso(nombre=data_formulario['nombre'], comision=data_formulario['comision'])
            curso.save()
            return render(request, "Alumnos/inicio.html", {"exitoso": True})
       
      else: 
       #GET  
            return render(request, "Alumnos/form_curso.html")

def curso_formulario1(request):
      if request.method == 'POST':
            data_formulario: Dict = request.POST
            alumnos = Alumnos(nombre=data_formulario['nombre'], apellido=data_formulario['apellido'])
            alumnos.save()
            return render(request, "Alumnos/inicio.html", {"exitoso": True})
       
      else: 
       #GET  
            return render(request, "Alumnos/form_curso1.html")

def curso_formulario2(request):
      if request.method == 'POST':
            data_formulario: Dict = request.POST
            ubicacion = Ubicacion(barrio=data_formulario['barrio'], provincia=data_formulario['provincia'])
            ubicacion.save()
            return render(request, "Alumnos/inicio.html", {"exitoso": True})
       
      else: 
       #GET  
            return render(request, "Alumnos/form_curso2.html")

def busqueda_cursos(request):
      return render(request, "Alumnos/form_busqueda_curso.html")



def buscar(request):
      if request.GET["comision"]:
            comision = request.GET["comision"]
            cursos = Curso.objects.filter(comision__icontains=comision)
            return render(request, "Alumnos/cursos_filtrados.html", {'cursos': cursos})
      else:
            return render(request, "Alumnoscursos.html", {'cursos': []})
