from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from ToDoList.forms import TaskForm
from ToDoList.models import Task, Tag


# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "ToDoList/index.html"
    queryset = Task.objects.all()

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=request.POST.get("task_id"))
        if task.done:
            task.done = False
        else:
            task.done = True
        task.save()
        return redirect("todo:index")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    template_name = "ToDoList/tag_list.html"


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    template_name = "ToDoList/tag_form.html"
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
