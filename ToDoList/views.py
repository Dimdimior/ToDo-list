from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from ToDoList.models import Task, Tag


# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "todo_list/index.html"
    queryset = Task.objects.all()

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=request.POST.get("task_id"))
        if task.done:
            task.done = False
        else:
            task.done = True
        task.save()
        return redirect("todo:index")
