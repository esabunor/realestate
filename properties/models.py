from django.db import models

# Create your models here.
class Property(models.Model):
    property_type = models.ForeignKey("PropertyType")
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    carspace = models.IntegerField()
    date_available = models.DateField()
    furnished = models.BooleanField()
    suburb = models.TextField()
    bond = models.IntegerField()
    description = models.TextField()
    location = models.TextField()

    def __str__(self):
        return "Property type: %s, Price: %s, Agent: %s" % (self.property_type, self.price, self.agent)

class PropertyType(models.Model):
    type_of_property = models.TextField()

    def __str__(self):
        return self.type_of_property