from django.shortcuts import render, redirect
from django.http import HttpResponse
from services.auth.login_service import Log_in, Log_out

# Create your views here.
def login(request):
    return render(request, "login.html", {})

def login(request):
    return Log_in(request)

def logout(request):
    return Log_out(request)

def index(request):
    return render(request, "index.html", {})