"""MainApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('signin.urls')),
    path('signin/', include('signin.urls')),
    path('personal/', include('personal.urls')),
    path('main/', include('main.urls')),
    path('saloons/', include('saloons.urls')),
    path('shops/', include('shops.urls')),
    path('media/', include('media.urls')),
    path('appartaments/', include('appartaments.urls')),
    path('casino/', include('casino.urls')),
    path('signup/', include('signup.urls')),
    path('admin/', admin.site.urls),
]