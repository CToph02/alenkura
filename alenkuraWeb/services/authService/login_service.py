from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def Log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        
        if user.is_superuser:
            return HttpResponse('admin')
        
        elif user.is_staff:
            return HttpResponse('staff')
        
        else:
            return redirect('index')
    return render(request, 'login.html')

def Log_out(request):
    logout(request)
    return redirect('login')