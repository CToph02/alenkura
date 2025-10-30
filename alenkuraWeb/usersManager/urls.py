from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index_administracion', views.index_administracion, name='index_administracion'),
    path('index_docent', views.index_docent, name='index_docent'),
    path('docent', views.docent, name='docent'),
    path('add_student', views.addStudent, name='add_student'),
    path('create_docent', views.create_docent, name='create_docent'),
    path('create_student', views.create_student, name='create_student'),
    path('paci', views.paci, name='paci'),
    path('cursos', views.cursos, name='cursos'),
    path('notas', views.notas, name='notas'),
    path('listaestudiantes', views.listaestudiantes, name='lista_estudiantes'),
    path('listadocentes', views.listadocentes, name='listadocentes'),
    path('cursoPorNivel', views.cursoPorNivel, name='cursoPorNivel'),
    path('listaestudiantes/buscar_estudiante', views.buscar_estudiante, name='buscar_estudiante')
]
