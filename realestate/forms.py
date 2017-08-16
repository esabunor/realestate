from django import forms
from properties.models import PropertyType
class BuyPropertySearchForm(forms.Form):
    property_type = forms.ModelChoiceField(queryset=PropertyType.objects.all(), widget=forms.Select(attrs={'class':"form-control", "placeholder":"Property Type"}))
    maxprice = forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
    minprice = forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
    bedrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
    carspace = forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
    furnished = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':"form-control"}))
    suburb = forms.CharField(max_length=40)
    search_type = forms.CharField(max_length=30, widget=forms.HiddenInput(), initial='buy')

class RentPropertySearchForm(forms.Form):
    property_type = forms.ModelChoiceField(queryset=PropertyType.objects.all(), widget=forms.Select(attrs={'class':"form-control"}))
    maxprice = forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
    minprice = forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
    bedrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
    carspace = forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
    furnished = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':"form-control"}))
    suburb = forms.CharField(max_length=40)
    search_type = forms.CharField(max_length=30, widget=forms.HiddenInput(), initial='rent')