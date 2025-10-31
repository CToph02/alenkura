from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_director'),
    path('listadocentes', views.lista_docentes, name='lista_docentes'),
    path('add_student', views.add_student, name='add_student'),
    path('listaestudiantes', views.lista_estudiantes, name='lista_estudiantes'),
    path('create_docent', views.create_docent, name='create_docent'),
    path('create_student', views.create_student, name='create_student'),
    path('listaestudiantes/buscar_estudiante', views.buscar_estudiante, name='buscar_estudiante')
]