from django.urls import path

from task.views import (PositionCreateView, PositionDeleteView,
                        PositionListView, PositionUpdateView,
                        ProjectCreateView, ProjectDeleteView,
                        ProjectDetailView, ProjectListView, ProjectUpdateView,
                        TaskCreateView, TaskDeleteView, TaskDetailView,
                        TaskListView, TaskTypeCreateView, TaskTypeDeleteView,
                        TaskTypeListView, TaskTypeUpdateView, TaskUpdateView,
                        TeamCreateView, TeamDeleteView, TeamListView,
                        TeamUpdateView, WorkerCreateView, WorkerDeleteView,
                        WorkerDetailView, WorkerListView, WorkerUpdateView,
                        index)

urlpatterns = [
    path("", index, name="index"),

    path(
        "task-types/",
        TaskTypeListView.as_view(),
        name="task-type-list"
    ),

    path(
        "task-types/create",
        TaskTypeCreateView.as_view(),
        name="task-type-create"
    ),

    path(
        "task-types/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-type-update"
    ),

    path(
        "task-types/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete"
    ),

    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"
    ),

    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),

    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),

    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),

    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),

    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list"
    ),

    path(
        "positions/create/",
        PositionCreateView.as_view(),
        name="position-create"
    ),

    path(
        "positions/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update"
    ),

    path(
        "positions/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete"
    ),

    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list"
    ),

    path(
        "workers/create/",
        WorkerCreateView.as_view(),
        name="worker-create"
    ),

    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),

    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update"
    ),

    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete"
    ),

    path(
        "projects/",
        ProjectListView.as_view(),
        name="project-list"
    ),

    path(
        "projects/<int:pk>/",
        ProjectDetailView.as_view(),
        name="project-detail"
    ),

    path(
        "projects/create/",
        ProjectCreateView.as_view(),
        name="project-create"
    ),

    path(
        "projects/<int:pk>/update/",
        ProjectUpdateView.as_view(),
        name="project-update"
    ),

    path(
        "projects/<int:pk>/delete/",
        ProjectDeleteView.as_view(),
        name="project-delete"
    ),

    path(
        "teams/",
        TeamListView.as_view(),
        name="team-list"
    ),

    path(
        "teams/create/",
        TeamCreateView.as_view(),
        name="team-create"
    ),

    path(
        "teams/<int:pk>/update/",
        TeamUpdateView.as_view(),
        name="team-update"
    ),

    path(
        "teams/<int:pk>/delete/",
        TeamDeleteView.as_view(),
        name="team-delete"
    ),

]

app_name = "task"
