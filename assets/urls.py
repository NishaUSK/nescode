from django.urls import path
from . import views

urlpatterns = [
    path('', views.electronicgadgets_list, name='electronicgadgets_list'),
    path('electronicgadgets/<int:pk>/', views.electronicgadgets_detail, name='electronicgadgets_detail'),

    path('', views.cars_list, name='cars_list'),
    path('kitchen/<int:pk>/', views.kitchen_detail, name='kitchen_detail'),


    path('', views.furnitures_list, name='furnitures_list'),
    path('furnitures/<int:pk>/', views.furnitures_detail, name='furnitures_detail'),

    path('', views.plasticmaterials_list, name='plasticmaterials_list'),
    path('plasticmaterials/<int:pk>/', views.plasticmaterials_detail, name='plasticmaterials_detail'),

    path('', views.kitchen_list, name='kitchen_list'),
    path('cars/<int:pk>/', views.cars_detail, name='cars_detail'),

]
