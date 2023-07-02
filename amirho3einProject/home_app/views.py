from django.shortcuts import render
from project_app.models import Project
from contactus_app.models import Info, Message
from service_app.models import Services


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        Message.objects.create(name=name, email=email, massage=massage)

    projects = Project.objects.all()
    info = Info.objects.all().last()
    service = Services.objects.all()

    return render(request, 'home_app/index.html', context={'projects': projects, 'info': info, 'service': service})
