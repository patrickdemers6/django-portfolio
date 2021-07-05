from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from .models import Experience


def home(request: HttpRequest) -> HttpResponse:
    experiences = Experience.objects.all()
    return render(request, 'experiences/home.html', {'experiences': experiences
                                                     })


def detail(request: HttpRequest, experience_id) -> HttpResponse:
    experience = get_object_or_404(Experience, pk=experience_id)
    return render(request, 'experiences/details.html', {'experience': experience})
