import re
from django.shortcuts import render, get_object_or_404

from .models import appimage

from django.http import HttpResponse

def home(request):
    images = appimage.objects
    return render(request, "app_gallery/home.html",{'images':images})

def details(request,image_id):
    app_image = get_object_or_404(appimage,pk = image_id)
    return render(request, "app_gallery/details.html", {"app_image":app_image})