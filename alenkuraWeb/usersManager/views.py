from django.shortcuts import render, redirect
from django.http import HttpResponse
from .services.auth_service import log_in, log_out
from .services.add_docent import create_docent

# Create your views here.
def login(request):
    return log_in(request)

def logout(request):
    return log_out(request)

def addDocent(request):
    return render(request, "userManager/add_docent.html")

def create_docent(request):
    return create_docent(request)


def index_director(request):
    return render(request, "index_director.html")