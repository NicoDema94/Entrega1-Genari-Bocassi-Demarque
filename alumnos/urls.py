from django.urls import path

from alumnos import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('ubicacion/', views.ubicacion, name="ubicacion"),
    path('curso/', views.curso, name="curso"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('crear-curso/', views.curso_formulario, name="curso_formulario"),
    path('crear-curso1/', views.curso_formulario1, name="curso_formulario1"),
    path('crear-curso2/', views.curso_formulario2, name="curso_formulario2"), 
    path('busqueda-curso/', views.buscar, name="busqueda_curso"),
    path('busqueda_curso_form/', views.busqueda_cursos, name="busqueda_curso_form"),
]
