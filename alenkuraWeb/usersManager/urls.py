from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index_director', views.index_director, name='index_director'),
    path('add_docent', views.addDocent, name='add_docent'),
    path('create_docent', views.create_docent, name='create_docent')
]
