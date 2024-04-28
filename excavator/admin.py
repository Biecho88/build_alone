from django.contrib import admin
from .models import Excavator

# Register your models here.

class ExcavatorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'model',
        'production_year',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)
admin.site.register(Excavator, ExcavatorAdmin)
