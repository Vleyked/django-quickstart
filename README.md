# django-quickstart


Create and activate your virtual env | (Configure the interpreter in vscode) | pi install django
Create a new django project
django-admin startproject myproject
cd myproject
3.  Run the development server so you can confirm that the project has been created succesfully
python manage.py runserver
4. Create a New app
python manage.py startapp myapp
5. Define a Model in myapp/models.py
from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
6. Registering the model with the Admin Site in myapp/admin.py
from django.contrib import admin

from .models import Task

# Register your models here.
admin.site.register(Task) 
7. include the app in the project in myproject/settings.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myapp",
]
8. Run the migration
python manage.py makemigrations
python manage.py migrate
9. Modifying the views (The logic of the front end) in myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the quickstar_first_steps index.")
10. Modify the urls so the user going to the main endpoint of your app can see this view (www.myapp.com/<We are modiying this view>) in myproject/ursl.py
from django.contrib import admin
from django.urls import path
from quickstart_first_step import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
]
11. Last step! Start the application
python manage.py runserver