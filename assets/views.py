from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Electronicgadgets
from .models import Kitchen
from .models import Furnitures
from .models import Plasticmaterials
from .models import Cars

def electronicgadgets_list(request):
    Electronicgadgets.objects.filter(launch_date__lte=timezone.now()).order_by('launch_date')
    return render(request, 'assets/electronicgadgets_list.html', {'Electronicgadgets': Electronicgadgets})

def electronicgadgets_detail(request, pk):
    Electronicgadgets = get_object_or_404(Electronicgadgets, pk=pk)
    return render(request, 'assets/electronicgadgets_detail.html', {'Electronicgadgets': Electronicgadgets})


def kitchen_list(request):
    Kitchen.objects.filter(expiry_date__lte=timezone.now()).order_by('manufactured_date')
    return render(request, 'assets/kitchen_list.html', {'Kitchen': Kitchen})

def kitchen_detail(request, pk):
    Kitchen = get_object_or_404(Kitchen, pk=pk)
    return render(request, 'assets/kitchen_detail.html', {'Kitchen': Kitchen})


def furnitures_list(request):
    Furnitures.objects.order_by('prize')
    return render(request, 'assets/furnitures_list.html', {'Furnitures': Furnitures})

def furnitures_detail(request, pk):
    Furnitures = get_object_or_404(Post, pk=pk)
    return render(request, 'assets/furnitures_detail.html', {'Furnitures': Furnitures})

def plasticmaterials_list(request):
    Plasticmaterials.objects.order_by('prize')
    return render(request, 'assets/plasticmaterials_list.html', {'Plasticmaterials': Plasticmaterials})

def plasticmaterials_detail(request, pk):
    Plasticmaterials = get_object_or_404(Plasticmaterials, pk=pk)
    return render(request, 'assets/plasticmaterials_detail.html', {'Plasticmaterials': Plasticmaterials})

def cars_list(request):
    Cars.objects.order_by('launch_date')
    return render(request, 'assets/cars_list.html', {'Cars': Cars})

def cars_detail(request, pk):
    Cars = get_object_or_404(Cars, pk=pk)
    return render(request, 'assets/cars_detail.html', {'Cars': Cars})
