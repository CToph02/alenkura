from django.shortcuts import render, redirect

def add_student(request):
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

def search_student(request, id):
    pass