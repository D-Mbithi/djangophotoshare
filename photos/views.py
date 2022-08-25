from re import template
from django.shortcuts import render
from .models import Photo

# Create your views here.
def home(request):
    photos = Photo.objects.all()
    context = {
        'images': photos
    }
    template = 'index.html'

    return render(request, template, context)

def photo_detail(request, pk):
    photo = Photo.objects.get(pk=pk)
    template = 'photos/detail.html'

    context = {
        'photo': photo
    }

    return render(request, template, context)