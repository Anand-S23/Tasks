from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Task, Category
from .forms import TaskForm
from django.contrib import messages

# Create your views here.
def home(request):
    # Handling form input 
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            description = form.cleaned_data.get('description')
            messages.success(request, f"New task created: {description}")
            return HttpResponseRedirect("/")
        else:
            messages.error(request, "Task not added, input vaild information.")

    # blank form         
    form = TaskForm()
         
    # All the tasks (from the model)
    tasks = Task.objects.all().order_by("due")

    # Context variable
    context = {
        'form':form,
        'tasks':tasks,
    }

    # Rendering everything to html (template)
    return render(request=request,
                  template_name='main/home.html',
                  context=context)


def delete_task(request, pk):
    #  Deleting the task
    dt = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        dt.delete()
        messages.success(request, 'Task deleted.')
        return HttpResponseRedirect('/')

    
    # Rendering everything to html (template)
    return render(request=request,
                  template_name='main/delete.html')
