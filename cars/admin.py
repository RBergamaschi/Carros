from django.contrib import admin
from cars.models import Car, Brand

class car_modelAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'plate')
    search_fields = ('model', 'brand')
    
class brand_modelAdmin(admin.ModelAdmin):
    list_display =('name',)
    search_fields = ('name',)


admin.site.register(Car, car_modelAdmin)
admin.site.register(Brand, brand_modelAdmin)