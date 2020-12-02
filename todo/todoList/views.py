from django.shortcuts import get_object_or_404, render, redirect

from .models import Task
from .forms import TaskForm

def index(request):
    task_list = Task.objects.order_by('-created_date')

    form = TaskForm()

    context = {
        'task_list': task_list,
        'form': form,
    }

    if request.method == 'POST':
            form = TaskForm(request.POST)

            if form.is_valid():
                form.save(commit=True)
                return render(request, 'index.html', context)
            else:
                print(form.errors)

    return render(request, 'index.html', context)


def done(request, id):
    task = get_object_or_404(Task, id = id)

    task.is_done = True
    task.save()

    return redirect('index')

def delete(request, id):
    task = get_object_or_404(Task, id = id)

    task.delete()
    return redirect('index')
