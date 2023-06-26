from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, "about/info.html")


def privacy(request):
    return render(request, "about/info.html")


def terms(request):
    return render(request, "about/info.html")
