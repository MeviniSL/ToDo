from django.shortcuts import render, redirect
from todo.models import Task 


def home(request):
    # handle form submission
    if request.method == 'POST':
        task_text = request.POST.get('task')
        if task_text:
            Task.objects.create(task=task_text)
        return redirect('home')

    # show pending tasks
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks': tasks,
    }
    return render(request, 'home.html', context)