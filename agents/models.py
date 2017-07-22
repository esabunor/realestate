from django.db import models
from django.conf import settings

# Create your models here.
class Agent(models.Model):
    company_name = models.TextField()
    email = models.EmailField()
    phone_number = models.IntegerField()
    #properties = models.ManyToManyField(Property)
    profile_image = models.ImageField(upload_to="profilephotos")
    about = models.TextField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)