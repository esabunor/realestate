from django.db import models

# Create your models here.
class RentProperty(models.Model):
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
    property_image1 = models.ImageField(upload_to='rentproperties')
    property_image2 = models.ImageField(blank=True, upload_to='rentproperties')
    property_image3 = models.ImageField(blank=True, upload_to='rentproperties')
    property_image4 = models.ImageField(blank=True, upload_to='rentproperties')
    property_image5 = models.ImageField(blank=True, upload_to='rentproperties')
    property_image6 = models.ImageField(blank=True, upload_to='rentproperties')
    property_image7 = models.ImageField(blank=True, upload_to='rentproperties')
    property_image8 = models.ImageField(blank=True, upload_to='rentproperties')
    property_image8 = models.ImageField(blank=True, upload_to='rentproperties')
    property_image9 = models.ImageField(blank=True, upload_to='rentproperties')

    def __str__(self):
        return "Property type: %s, Price: %s" % (self.property_type, self.price)

class PropertyType(models.Model):
    type_of_property = models.TextField()

    def __str__(self):
        return self.type_of_property


class BuyProperty(models.Model):
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
    property_image1 = models.ImageField(blank=True, upload_to='buyproperties')
    property_image2 = models.ImageField(blank=True, upload_to='buyproperties')
    property_image3 = models.ImageField(blank=True, upload_to='buyproperties')
    property_image4 = models.ImageField(blank=True, upload_to='buyproperties')
    property_image5 = models.ImageField(blank=True, upload_to='buyproperties')
    property_image6 = models.ImageField(blank=True, upload_to='buyproperties')
    property_image7 = models.ImageField(blank=True, upload_to='buyproperties')
    property_image8 = models.ImageField(blank=True, upload_to='buyproperties')
    property_image8 = models.ImageField(blank=True, upload_to='buyproperties')
    property_image9 = models.ImageField(blank=True, upload_to='buyproperties')

    def __str__(self):
        return "Property type: %s, Price: %s" % (self.property_type, self.price)