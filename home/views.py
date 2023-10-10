from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def faqs(request):
    return render(request, 'home/faqs.html')


def courses(request):
    return render(request, 'home/courses.html')


def about(request):
    return render(request, 'home/about.html')