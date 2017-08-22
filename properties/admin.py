from django.contrib import admin
from .models import PropertyType, BuyProperty, RentProperty
# Register your models here.

class BuyPropertyAdmin(admin.ModelAdmin):
    list_display = ('property_type', 'price', 'bedrooms', 'suburb')

class RentPropertyAdmin(admin.ModelAdmin):
    list_display = ('property_type', 'price', 'bedrooms', 'suburb')

class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('type_of_property',)

admin.site.register(BuyProperty, BuyPropertyAdmin)
admin.site.register(RentProperty, RentPropertyAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)