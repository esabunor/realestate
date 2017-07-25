from django.contrib import admin
from .models import PropertyType, BuyProperty, RentProperty
# Register your models here.

class BuyPropertyAdmin(admin.ModelAdmin):
    list_display = ()

class RentPropertyAdmin(admin.ModelAdmin):
    list_display = ()

class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ()

admin.site.register(BuyProperty, BuyPropertyAdmin)
admin.site.register(RentProperty, RentPropertyAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)