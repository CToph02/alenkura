from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
    
    # path('paci', views.paci, name='paci'),
    # path('cursos', views.cursos, name='cursos'),
    # path('notas', views.notas, name='notas'),
    
    # path('cursoPorNivel', views.curso_por_nivel, name='cursoPorNivel'),
    
]
