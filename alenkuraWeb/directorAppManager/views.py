from django.http import HttpResponse
from django.shortcuts import render
from usersManager.models import User
from docentAppManager.models import Student, StudentParent
from directorAppManager.services.docent_service import create_docent, get_curso_por_nivel
from directorAppManager.services.student_service import create_student, search_student
# Create your views here.
def index(request):
    return render(request, 'index_director.html')

def lista_docentes(request):
    usuarios = User.objects.all()
    context = {
        "usuarios": usuarios
    }
    return render(request, "listadocentes.html", context)

def lista_estudiantes(request):
    estudiantes = Student.objects.all()
    context = {
        "estudiantes": estudiantes
    }
    return render(request, "listaestudiantes.html", context)

def add_student(request):
    return render(request, "userManager/add_student.html")

def create_docent(request):
    return create_docent(request)

def create_student(request):
    return create_student(request)

def buscar_estudiante(request):
    return search_student(request)

def curso_por_nivel(request):
    return get_curso_por_nivel(request)