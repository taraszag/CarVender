from django.contrib import admin
from .models import Sellrequest, Carmodel, Carvender

# Register your models here.
admin.site.register(Sellrequest)
admin.site.register(Carvender)
admin.site.register(Carmodel)


