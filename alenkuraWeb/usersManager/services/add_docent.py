from django.shortcuts import render, redirect

def create_docent(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')

    print(username, email, phone)
    return redirect('add_docent')