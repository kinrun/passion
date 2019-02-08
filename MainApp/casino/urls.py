from django.urls import path

from . import views

app_name = 'casino'
urlpatterns = [
    path('', views.index, name='index'),
]