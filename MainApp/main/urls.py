from django.urls import path

from . import views
from personal.views import newuser

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.index, name='main'),
    path('sellers/', views.sellers, name='sellers'),
    path('saloons/', views.saloons, name='saloons'),    
    path('logout/', views.log_out, name='logout'),
    path('newuser/', newuser, name='newuser'),
]