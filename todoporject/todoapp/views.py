from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
# Create your views here.


def addTask(request):
    tasking = request.POST['tasked']   #This tasked is located from home.html represent input tag of name
    Task.objects.create(task=tasking)  #forward **task** is model task
    return redirect('home')


def mark(reques,pk):
    mark = get_object_or_404(Task, pk=pk) #forward 'pk' is the filed name of the task model and last 'pk' is dynamic primary key that we are passing from the url bar.
    mark.is_completed = True # is_completed is in the model field name
    mark.save()
    return redirect('home')


def unmark(reques,pk):
    unmark = get_object_or_404(Task, pk=pk) #forward 'pk' is the filed name of the task model and last 'pk' is dynamic primary key that we are passing from the url bar.
    unmark.is_completed = False # is_completed is in the model field name
    unmark.save()
    return redirect('home')

def taskedit(request,pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_task =request.POST['tasked']
        get_task.task =new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request,'edit.html', context)
    
    
def taskdelete(request,pk):
    delete = get_object_or_404(Task, pk=pk)
    delete.delete()
    return redirect('home')