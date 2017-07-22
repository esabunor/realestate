from django.shortcuts import render

def property_details_view(request):
    return render(request, "propertydetails.html")
