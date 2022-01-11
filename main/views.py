from django.shortcuts import render
from .models import Project
from django.contrib import messages


def home(request):
    projects = Project.objects.all()
    if request.method == "POST":
        messages.success(request, 'Form submission successful')
    context = {
        'projects': projects,
        'total_projects': len(projects),
    }

    return render(request, 'main/home.html', context)
