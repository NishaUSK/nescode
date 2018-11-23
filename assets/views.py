from django.shortcuts import render
# from django.utils import timezone
# from .models import Electronicgadgets
# from .models import Kitchen
# from .models import Furnitures
# from .models import Plasticmaterials
# from .models import Cars

def electronicgadgets_list(request):
    # electronicgadgets.objects.filter(launch_date__lte=timezone.now()).order_by('launch_date')
    return render(request, 'assets/electronicgadgets_list.html', {})
