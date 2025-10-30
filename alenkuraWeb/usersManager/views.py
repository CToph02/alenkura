#from django.contrib.auth.models import User
#from .models import Curso
from .models import User
from coreBD.models import Curso, Rol
from django.shortcuts import render
from .services.auth_service import log_in, log_out
from .services.docent_service import create_docent, get_curso_por_nivel
from .services.student_service import create_student, search_student

# Create your views here.
def login(request):
    return log_in(request)

def logout(request):
    return log_out(request)

def docent(request):
    rol = Rol.objects.exclude(rol='Director')
    cursos = Curso.objects.all()

    context = {
        'rol': rol,
        'curso': cursos
    }

    return render(request, "userManager/add_docent.html", context)

def addStudent(request):
    return render(request, "userManager/add_student.html")

def create_docent(request):
    return create_docent(request)

def create_student(request):
    return create_student(request)

def index_administracion(request):
    return render(request, "index_administracion.html")

def index_docent(request):
    return render(request, "index_docent.html")

def paci(request):
    return render(request, "paci.html")

def cursos(request):
    return render(request, "cursos.html")

def notas(request):
    return render(request, "notas.html")

def listaestudiantes(request):
    usuarios = User.objects.all()
    context = {
        "usuarios": usuarios
    }
    return render(request, "listaestudiantes.html", context)

def listadocentes(request):
    usuarios = User.objects.all()
    context = {
        "usuarios": usuarios
    }
    return render(request, "listadocentes.html", context)

def cursoPorNivel(request):
    return get_curso_por_nivel(request)

def buscar_estudiante(request):
    return search_student(request)