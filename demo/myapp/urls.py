from django.urls import path
from . import views
from django.conf import settings  # <-- add this
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todo_list, name="todo_list"),
    path("todos/add/", views.add_todo, name="add_todo"),
    path("todos/complete/<int:todo_id>/",
         views.complete_todo, name="complete_todo"),
    path("todos/delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),
    path("todos/edit/<int:todo_id>/", views.edit_todo, name="edit_todo"),
    path("todos/clear/", views.clear_completed, name="clear_completed"),
    path("todos/uncomplete/<int:todo_id>/",
         views.uncomplete_todo, name="uncomplete_todo"),
]

if settings.DEBUG:  # now settings is defined
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
