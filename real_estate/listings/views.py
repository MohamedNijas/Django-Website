from django.shortcuts import render,redirect
from .models import Listings
from .forms import ListingForm

# Create your views here.
#CRUD = create,retrive,update,delete
def listings_list(request):
    listings = Listings.objects.all()
    context  = {
        "listings":listings
    }
    return render(request,"listings.html",context)

def listing_retrive(request,pk):
    Listing = Listings.objects.get(id = pk)
    context = {
        "listing":Listing #here u need to use the dictionary key in the html file
    }
    return render(request,"retrive.html",context)
def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form
    }
    return render(request,"listing_request.html",context)


def listing_update(request,pk):
    listing = Listings.objects.get(id = pk)
    form = ListingForm(instance = listing)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form
    }
    return render(request,"listing_update.html",context)

def delete_listing(request,pk):
    listing = Listings.objects.get(id = pk)
    listing.delete()
    return redirect("/")



