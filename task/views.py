import json
from typing import Any, Dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from task.forms import TaskForm, TaskSearchForm, TaskTypeSearchForm, WorkerCreationForm, PositionSearchForm, WorkerSearchForm

from task.models import TaskType, Position, Worker, Task

# Create your views here.

# @login_required
def index(request):
    num_task_type = TaskType.objects.count()
    num_position = Position.objects.count()
    num_worker = Worker.objects.count()
    num_task = Task.objects.count()
   
    context = {
        "num_position": num_position,
        "num_worker": num_worker,
        "num_task": num_task,
        "num_task_type": num_task_type,
    }
    


    return render(request, "task/index.html", context=context)


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "task/task_type_list.html"
    context_object_name = "task_type_list"
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(TaskTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskTypeSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = TaskType.objects.all()
        form = TaskTypeSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields ="__all__"
    success_url = reverse_lazy("task:task-type-list")
    template_name = "task/task_type_form.html"


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields ="__all__"
    success_url = reverse_lazy("task:task-type-list")
    template_name = "task/task_type_form.html"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task:task-type-list")
    template_name = "task/task_type_confirm_delete.html"


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(TaskListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")
        context["search_form"] = TaskSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Task.objects.select_related("task_type")
        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset

class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    queryset = Task.objects.select_related("task_type")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    queryset = Task.objects.select_related("task_type")
    form_class = TaskForm


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
   

class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(PositionListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = PositionSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Position.objects.all()
        form = PositionSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields ="__all__"
    success_url = reverse_lazy("task:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields ="__all__"
    success_url = reverse_lazy("task:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task:position-list")
    template_name = "task/position_confirm_delete.html"

class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = WorkerSearchForm(
            initial={
                "username": username
            }
        )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Worker.objects.all()
        form = WorkerSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])
        return queryset


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("task:worker-list")
