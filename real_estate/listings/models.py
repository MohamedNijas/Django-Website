from django.db import models

# Create your models here.
class Listings (models.Model):
    title = models.CharField(max_length = 1000)
    price = models.IntegerField()
    no_of_bathrooms = models.IntegerField()
    no_of_bedrooms  = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length = 150)
    image = models.ImageField()
    def __str__(self):
        return self.title


