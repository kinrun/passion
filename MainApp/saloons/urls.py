from django.urls import path

from . import views

app_name = 'saloons'
urlpatterns = [
    path('', views.index, name='index'),
]