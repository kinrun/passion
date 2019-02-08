from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.index, name='index'),
    path('myorders/', views.my_orders, name='my_orders'),
    # example: /orders/new/5/
    path('new/<int:seller_id>/', views.new_order, name='new_order'),
]