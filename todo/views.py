from .models import Task
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def addTask(request):
    task = (request.POST['task'])
    Task.objects.create(task=task)
    return redirect('home')