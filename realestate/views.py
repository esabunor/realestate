from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import BuyPropertySearchForm, RentPropertySearchForm
from properties.models import BuyProperty, RentProperty
def search_view(request):
    buyform = BuyPropertySearchForm()
    rentform = RentPropertySearchForm()
    search_view_dict = {"buyform":buyform, "rentform":rentform}
    return render(request, "search.html", search_view_dict)

def result_view(request):
    properties = ""
    form = ""
    search_type = ""
    result_view_dict = {}
    if request.method == "POST":
        if 'search_type' in request.POST:
            if request.POST['search_type'] == 'buy':
                search_type = 'buy'
                form = BuyPropertySearchForm(request.POST)
            else:
                form = RentPropertySearchForm(request.POST)
            if form.is_valid():
                if search_type == 'buy':
                    properties = BuyProperty.objects.filter(property_type=form.property_type, price__lte=form.maxprice, price__gte=form.minprice, bedrooms=form.bedrooms, carspace=form.carspace, furnished=form.furnished, surburb=form.suburb)
                else:
                    properties = RentPropertySearchForm.objects.filter(property_type=form.property_type, price__lte=form.maxprice, price__gte=form.minprice, bedrooms=form.bedrooms, carspace=form.carspace, furnished=form.furnished, surburb=form.suburb)
                
                result_view_dict = {"properties":properties}
        else:
            Http404()
    else:
        HttpResponseRedirect(reverse('search_view'))
    return render(request, "results.html")