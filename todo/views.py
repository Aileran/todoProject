from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


#render index page
def index(request):
    # get all task objects, render them on index
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)


#render update page
def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {'form': form, 'task': task}
    return render(request, 'todo/update.html', context)


#render delete page
def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return redirect('index')
    context = {'task': task}
    return render(request, 'todo/delete.html', context)


# add a task to the list
def add(request):
    if request.method == "POST":
        task = request.POST.get('task')
        Task.objects.create(task=task)
        return redirect('index')
    else:
        return render(request, 'todo/index.html')


# mark task passed as complete
def complete(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('index')