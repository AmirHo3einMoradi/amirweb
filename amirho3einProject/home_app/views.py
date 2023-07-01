from django.shortcuts import render
from project_app.models import Project
from contactus_app.models import Info, Message


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        Message.objects.create(name=name, email=email, massage=massage)

    projects = Project.objects.all()
    info = Info.objects.all().last()

    return render(request, 'home_app/index.html', context={'projects': projects, 'info': info})
