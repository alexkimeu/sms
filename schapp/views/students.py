from django.shortcuts import render
from django.views.generic import ListView
from ..models import Grade


def student_profile(request):
    grades = Grade.objects.all()
    return render(request, 'schapp/students/index.html', {'grades': grades})
