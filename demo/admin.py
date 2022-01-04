from django.contrib import admin

# Register your models here.
from .models import Demo, SortingMethod

admin.site.register(Demo)
admin.site.register(SortingMethod)
