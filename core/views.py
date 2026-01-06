from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project
from .forms import ContactForm


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def projects(request):
    items = Project.objects.order_by("-created_at")
    return render(request, "core/projects.html", {"projects": items})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pesan Kamu sudah terkirim. Makasih ya!")
            return redirect("contact")

    else:
            form = ContactForm()

    return render(request, "core/contact.html", {"form": form})
