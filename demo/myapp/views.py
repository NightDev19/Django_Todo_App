from django.shortcuts import render, get_object_or_404
from .models import TodoItem


def home(request):
    return render(request, 'home.html')


def todo_list(request):
    todoList = TodoItem.objects.all()
    return render(request, 'todos.html', {"todos": todoList})


def add_todo(request):
    if request.method == "POST":
        todo = TodoItem(title=request.POST['title'])
        todo.save()
    return render(request, 'todos.html', {"todos": TodoItem.objects.all()})


def complete_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(TodoItem, pk=todo_id)
        todo.completed = True
        todo.save()
    return render(request, 'todos.html', {"todos": TodoItem.objects.all()})


def uncomplete_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(TodoItem, pk=todo_id)
        todo.completed = False
        todo.save()
    return render(request, 'todos.html', {"todos": TodoItem.objects.all()})


def delete_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(TodoItem, pk=todo_id)
        todo.delete()
    return render(request, 'todos.html', {"todos": TodoItem.objects.all()})


def edit_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(TodoItem, pk=todo_id)
        todo.title = request.POST['title']
        todo.save()
    return render(request, 'todos.html', {"todos": TodoItem.objects.all()})


def clear_completed(request):
    if request.method == "POST":
        TodoItem.objects.filter(completed=True).delete()
    return render(request, 'todos.html', {"todos": TodoItem.objects.all()})
