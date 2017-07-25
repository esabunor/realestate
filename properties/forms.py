from django.forms import ModelForm
from properties.models import BuyProperty, RentProperty
class BuyPropertyForm(ModelForm):
    """
    This class represents a form accessible to agents allowing them to upload their 
    properties
    """
    class Meta:
        model = BuyProperty
        fields = '__all__'
        widgets = {
            'description' : Textarea()
        }