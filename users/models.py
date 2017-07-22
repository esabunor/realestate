from django.db import models
from django.conf import settings
from properties.models import Property

# Create your models here.
class SiteUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    saved_properties = models.ManyToManyField(Property)