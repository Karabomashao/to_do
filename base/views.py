from django.shortcuts import render, get_object_or_404
from .models import tasklist
from .forms import RawProductForm, Taskform

def tasks(request):
    all_objects = tasklist.objects.all()
    context = {
        "obj" : all_objects
    }
    return render(request, 'Homepage.html', context)


def task_detailed_view(request, item_id):
    item = get_object_or_404(tasklist, pk=item_id)
    return render(request, 'task_detailed_view.html', {'item' : item})


def task_create_view(request):
    my_form = Taskform(request.POST or None)
    if my_form.is_valid():   
        my_form.save()
        my_form = Taskform()
    context = {
    "my_form" : my_form
    }
    return render(request, "create_view.html", context)