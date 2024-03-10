from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task
# Create your views here.


def addTask(request):
    tasking = request.POST['tasked']   #This tasked is located from home.html represent input tag of name
    Task.objects.create(task=tasking)  #forward **task** is model task
    return redirect('home')