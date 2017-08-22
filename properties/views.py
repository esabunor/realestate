from django.shortcuts import render
from .models import BuyProperty, RentProperty
"""
This view is responsible for showing the details of a property
"""
def property_details_view(request, suburb=None, id=None, property_type=None, search_type=None):
    
    return render(request, "propertydetails.html")
