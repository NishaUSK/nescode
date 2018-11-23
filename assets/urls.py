from django.urls import path
from . import views

urlpatterns = [
    path('', views.electronicgadgets_list, name='electronicgadgets_list'),
]
