from django.shortcuts import render


template_name = 'home_app\index.html'
def home(request):
    return render(request, template_name, {})
