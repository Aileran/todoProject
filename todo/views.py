from django.shortcuts import render, redirect
from .models import Task


#render index page
def index(request):
    # Query the to-do table and get all the records
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)


#render update page
def update(request):
    return render(request, 'todo/update.html')

#render delete page
def delete(request):
    return render(request, 'todo/delete.html')