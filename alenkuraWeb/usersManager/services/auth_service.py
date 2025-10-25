from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        
        if user.is_superuser:
            return redirect('index_administracion')
        
        elif user.is_staff:
            return redirect('index_docent')
            
    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('login')