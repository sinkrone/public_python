from django.shortcuts import render
from .models import Slide, Service, Condition


# Create your views here.


def home(request):
    slides = Slide.objects.all()
    services = Service.objects.all()
    conditions = Condition.objects.all()
    context = {
        "slide_list": slides,
        "service_list": services,
        "odd_condition_list": conditions[1::2],
        "even_condition_list": conditions[::2],
    }
    return render(request, "web/home.html", context)
