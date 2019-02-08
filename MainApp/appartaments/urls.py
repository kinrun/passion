from django.urls import path

from . import views

app_name = 'appartaments'
urlpatterns = [
    path('', views.index, name='index'),
]