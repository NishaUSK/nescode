from django.urls import path
from . import views

urlpatterns = [
    path('', views.electronicgadgets_list, name='electronicgadgets_list'),
    path('', views.cars_list, name='cars_list'),
    path('', views.furnitures_list, name='furnitures_list'),
    path('', views.plasticmaterials_list, name='plasticmaterials_list'),
    path('', views.kitchen_list, name='kitchen_list'),
]
