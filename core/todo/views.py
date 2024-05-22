from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.core.cache import cache
from .forms import TaskUpdateForm

from .models import Task
import requests



class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/task_list.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if cache.get("temp_of_tehran") is None:
            response=requests.get("https://api.openweathermap.org/data/2.5/weather?q=tehran&appid=7f5ad6244b2dffe8f996094746afa1fe")
            cache.set("temp_of_tehran",response.json(),20*60)
        response=cache.get("temp_of_tehran")
        context['cityname']=response["name"]
        context['citytemp']=round((response["main"]["temp"]-273),2)
        return context
    

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy("todo:task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy("todo:task_list")
    form_class = TaskUpdateForm
    template_name = "todo/update_task.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskComplete(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("todo:task_list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.success_url)


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("todo:task_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
