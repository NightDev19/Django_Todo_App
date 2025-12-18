from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todo_list, name="todo_list"),

    # ADD THESE
    path("todos/add/", views.add_todo, name="add_todo"),
    path("todos/complete/<int:todo_id>/",
         views.complete_todo, name="complete_todo"),
    path("todos/delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),
    path("todos/edit/<int:todo_id>/", views.edit_todo, name="edit_todo"),
    path("todos/clear/", views.clear_completed, name="clear_completed"),
    path("todos/uncomplete/<int:todo_id>/",
         views.uncomplete_todo, name="uncomplete_todo"),
]
