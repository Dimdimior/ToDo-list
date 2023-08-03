from django.urls import path

from ToDoList.views import (
    IndexView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskToggleView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("tag/create", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
    path("toggle_task/", TaskToggleView.as_view(), name="task-toggle"),
]

app_name = "ToDoList"
