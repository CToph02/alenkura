from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def log_in(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email)
    print(password)

    user = authenticate(email=email, password=password)

    print(user)

    if user is not None:
        login(request, user)
        print(user.rol)

        if user.is_superuser:
            return redirect('index_director')
        
        elif user.is_docent:
            return redirect('index_docent')
            
    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('login')