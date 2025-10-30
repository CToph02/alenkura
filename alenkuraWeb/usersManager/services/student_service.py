from django.http import HttpResponse
from django.shortcuts import render, redirect
from usersManager.models import User
from django.db.models import Q

def create_student(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    type = request.POST.get('typeDocent')

    print(username, email, phone, type)
    return redirect('add_docent')

def delete_student(request):
    pass

def update_student(request, id):
    pass

def search_student(request):
    if request.method == 'POST':
        query = request.POST.get('search_estudiante')
        if query:
            estudiante = User.objects.filter(Q(name__icontains=query))
            nombre_estudiante = estudiante.values_list('name', flat=True)
            print(nombre_estudiante[0])
        else:
            nombre_estudiante = User.objects.all()
    return render(request, 'listaestudiantes.html', {"estudiante": nombre_estudiante[0]})