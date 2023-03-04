from django.forms import ModelForm
from .models import Listings

class ListingForm(ModelForm):
    class Meta:
        model = Listings
        fields = [
            "title", 
            "price", 
            "no_of_bedrooms",
            "no_of_bathrooms",  
            "square_footage",
            "address",
            "image"
        ]

        