from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('deadline')
    completed = sum(1 for t in tasks if t.status)
    pending = sum(1 for t in tasks if not t.status)
    context = {'tasks': tasks, 'completed': completed, 'pending': pending}
    return render(request, 'task_list.html', context)



def add_task(request):
    if request.method == 'POST':
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST.get('description', ''),
            category=request.POST['category'],
            deadline=request.POST.get('deadline', None),
            priority=request.POST['priority']
        )
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.category = request.POST['category']
        task.deadline = request.POST.get('deadline', None)
        task.priority = request.POST['priority']
        task.status = 'status' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/edit_task.html', {'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
