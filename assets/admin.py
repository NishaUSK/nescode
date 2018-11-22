from django.contrib import admin
from .models import Electronicgadgets
from .models import Kitchen
from .models import Furnitures
from .models import Plasticmaterials
from .models import Cars

admin.site.register(Electronicgadgets)
admin.site.register(Kitchen)
admin.site.register(Furnitures)
admin.site.register(Plasticmaterials)
admin.site.register(Cars)
