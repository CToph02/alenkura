#from django.contrib.auth.models import User
#from .models import Curso
from django.http import HttpResponse
from .models import User
from docentAppManager.models import Student, StudentParent
from coreBD.models import Curso, Rol
from django.shortcuts import render
from .services.auth_service import log_in, log_out

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

def paci(request):
    return render(request, "paci.html")

def cursos(request):
    return render(request, "cursos.html")

def notas(request):
    return render(request, "notas.html")