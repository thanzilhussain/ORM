from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'manufacturer', 'model_name', 'year', 'price')
    list_filter = ('year', 'manufacturer')
    search_fields = ('model_name', 'manufacturer')

admin.site.register(Car, CarAdmin)


