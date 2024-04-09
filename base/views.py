from django.shortcuts import render
from .models import tasklist

def tasks(request):

    all_objects = tasklist.objects.all()

    context = {
        "obj" : all_objects
    }
    return render(request, 'Homepage.html', context)
