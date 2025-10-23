from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('director_dashboard', views.director_dashboard, name='director_dashboard'),
    path('docent_dashboard', views.docent_dashboard, name='docent_dashboard')
]
