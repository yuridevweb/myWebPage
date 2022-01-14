from django.shortcuts import render, redirect
from .models import Project
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    projects = Project.objects.all()
    for p in projects:
        print(p.made_with)

    if request.method == "POST":
        form_data = list(request.POST.items())
        name = form_data[1][1]
        email = form_data[2][1]
        subject = form_data[3][1]
        raw_message = form_data[4][1]
        recipient = 'yuridevweb@gmail.com'
        message = raw_message + "\nName: " + name + "\nEmail: " + email

        send_mail(subject, message,
                  settings.DEFAULT_FROM_EMAIL, [recipient])

        messages.success(request, 'Form submission successful')
        return redirect('home')

    context = {
        'projects': projects,
        'total_projects': len(projects),
    }

    return render(request, 'main/home.html', context)
