from django.contrib import admin
from .models import Item

# Register your models here.

# register Item model with admin site
admin.site.register(Item)
