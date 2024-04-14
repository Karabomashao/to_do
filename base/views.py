from django.shortcuts import render, get_object_or_404, redirect
from .models import tasklist
from .forms import RawProductForm, Taskform, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password=password)
            if user is not None:
                print("came here")
                login(request, user)
                return redirect("/")
            else:
                form.add_error("/")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form' : form})

def logout_view(request):
    print("you have been logged out")
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def tasks(request):
    all_objects = tasklist.objects.filter(user_auth=request.user)
    context = {
        "obj" : all_objects
    }
    return render(request, 'Homepage.html', context)

@login_required(login_url='login')
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


@login_required(login_url='login')
def task_update_view(request, item_id):
    instance = get_object_or_404(tasklist, pk=item_id)
    if request.method == 'POST':
        update_form = Taskform(request.POST, instance=instance)
        if update_form.is_valid():
            update_form.save()
            return redirect('/')
    else:
        update_form =Taskform(instance=instance)
        print("I opened the form")
    return render(request, "update_view.html", {'update_form': update_form})

@login_required(login_url='login')
def delete_task_views(request, item_id):
    obj= get_object_or_404(tasklist, pk=item_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    return render(request, "delete_view.html", {'obj': obj})
