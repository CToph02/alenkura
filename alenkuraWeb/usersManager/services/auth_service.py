from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    print(password)

    user = authenticate(name=username, password=password)

    print(user)

    if user is not None:
        login(request, user)
        print(user.rol)

        if user.is_superuser:
            return redirect('index_administracion')
        
        elif user.is_docent:
            return redirect('index_docent')
            
    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('login')