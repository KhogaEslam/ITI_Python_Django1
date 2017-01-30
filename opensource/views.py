from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Student, Track

def hello(request):
    return HttpResponse('Hello!!!')

def details(request, id):
    return HttpResponse('details of %s' %id)

def showAllStudents(request):
    allStudents = Student.objects.all()
    context = {'allStudents':allStudents}

    return render(request, 'opensource/index.html', context)
