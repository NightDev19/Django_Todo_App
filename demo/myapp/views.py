from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import TodoItem
import os


def home(request):
    return render(request, 'home.html')


def todo_list(request):
    todoList = TodoItem.objects.all().order_by('-id')
    paginator = Paginator(todoList, 5)  # 5 todos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'todos.html', {"todos": page_obj})


def add_todo(request):
    if request.method == "POST":
        todo = TodoItem(
            title=request.POST['title'],
            image=request.FILES.get('image')
        )
        todo.save()
    return redirect('todo_list')


def complete_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(TodoItem, pk=todo_id)
        todo.completed = True
        todo.save()
    return redirect('todo_list')


def uncomplete_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(TodoItem, pk=todo_id)
        todo.completed = False
        todo.save()
    return redirect('todo_list')


def delete_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(TodoItem, pk=todo_id)
        if todo.image:
            if os.path.isfile(todo.image.path):
                os.remove(todo.image.path)
        todo.delete()
    return redirect('todo_list')


def edit_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(TodoItem, pk=todo_id)
        todo.title = request.POST['title']
        if 'image' in request.FILES:
            if todo.image:
                if os.path.isfile(todo.image.path):
                    os.remove(todo.image.path)
            todo.image = request.FILES['image']
        todo.save()
    return redirect('todo_list')


def clear_completed(request):
    if request.method == "POST":
        completed_todos = TodoItem.objects.filter(completed=True)
        for todo in completed_todos:
            if todo.image:
                if os.path.isfile(todo.image.path):
                    os.remove(todo.image.path)
        completed_todos.delete()
    return redirect('todo_list')
