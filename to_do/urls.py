"""
URL configuration for to_do project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import tasks, task_detailed_view, task_create_view, task_update_view, delete_task_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tasks, name='tasks'),
    path('item/<int:item_id>/', task_detailed_view, name='item_detail'),
    path('create', task_create_view, name='tasks_create'),
    path('update/<int:item_id>/', task_update_view, name='update_task'),
    path('delete/<int:item_id>/', delete_task_views, name='delete_task'),

]
