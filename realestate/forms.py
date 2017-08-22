from django import forms
from properties.models import PropertyType
class BuyPropertySearchForm(forms.Form):
    property_type = forms.ModelChoiceField(queryset=PropertyType.objects.all(), widget=forms.Select(attrs={'class':"", "placeholder":"Property Type"}))
    maxprice = forms.IntegerField(widget=forms.NumberInput(attrs={'class':""}))
    minprice = forms.IntegerField(widget=forms.NumberInput(attrs={'class':""}))
    bedrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class':""}))
    carspace = forms.IntegerField(widget=forms.NumberInput(attrs={'class':""}))
    furnished = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':""}))
    suburb = forms.CharField(max_length=40)
    search_type = forms.CharField(max_length=30, widget=forms.HiddenInput(), initial='buy')

class RentPropertySearchForm(forms.Form):
    property_type = forms.ModelChoiceField(queryset=PropertyType.objects.all(), widget=forms.Select(attrs={'class':""}))
    maxprice = forms.IntegerField(widget=forms.NumberInput(attrs={'class':""}))
    minprice = forms.IntegerField(widget=forms.NumberInput(attrs={'class':""}))
    bedrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'class':""}))
    carspace = forms.IntegerField(widget=forms.NumberInput(attrs={'class':""}))
    furnished = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':""}))
    suburb = forms.CharField(max_length=40)
    search_type = forms.CharField(max_length=30, widget=forms.HiddenInput(), initial='rent')