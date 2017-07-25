from django.db import models
from django.conf import settings
from properties.models import BuyProperty, RentProperty

# Create your models here.
class SiteUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    buy_saved_properties = models.ManyToManyField(BuyProperty)
    rent_saved_properties = models.ManyToManyField(RentProperty)