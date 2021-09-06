from django.db import models
from django.shortcuts import render, redirect
from .models import Image, Location,Category
from django.http  import HttpResponse, Http404


# Create your views here.
def landing(request):
    
    title='Ultimate Gallery'
    return render(request, 'index.html', {'title': title})

def home(request):
    # location = Location.get_location()
    photos=Image.get_all_images()
    return render(request, 'home.html', {'photos': photos})

def photo_details(request, image_id):
    try:
        details = Image.objects.get(pk =image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"details.html", {"details":details})


def search_results(request):
    title="Find"
    locations = Location.objects.all()
    categories = Category.objects.all()
    
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"


        return render(request, 'search.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "locations":locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})