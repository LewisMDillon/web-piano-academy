from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def errortest400(request):
    return render(request, '400.html')


def errortest403(request):
    return render(request, '403.html')


def errortest404(request):
    return render(request, '404.html')


def errortest500(request):
    return render(request, '500.html')
