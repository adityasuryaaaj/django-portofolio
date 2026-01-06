from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request,"core/about.html")

def projects(request):
    items = Project.objects.order_by("-created_at")
    return render(request,"core/projects.html",{"projects":items})

def contact(request):
    return render(request,"core/contact.html")