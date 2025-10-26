from django.shortcuts import render, redirect
from django.contrib import messages

def add_docent(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    type = request.POST.get('typeDocent')

    print(username, email, phone, type)
    messages.success(request, "Se creó docente")
    return redirect('add_docent')

def delete_docent(request):
    pass

def update_docent(request, id):
    pass

def delete_docent(request, id):
    pass