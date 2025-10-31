from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add_student', views.add_student, name='add_student'),
    path('create_docent', views.create_docent, name='create_docent'),
    path('create_student', views.create_student, name='create_student'),
    path('paci', views.paci, name='paci'),
    path('cursos', views.cursos, name='cursos'),
    path('notas', views.notas, name='notas'),
    path('listaestudiantes', views.lista_estudiantes, name='lista_estudiantes'),
    path('listadocentes', views.lista_docentes, name='lista_docentes'),
    path('cursoPorNivel', views.curso_por_nivel, name='cursoPorNivel'),
    path('listaestudiantes/buscar_estudiante', views.buscar_estudiante, name='buscar_estudiante')
]
