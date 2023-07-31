from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="workers",
        null=True
    )

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}({self.position})"


class Task(models.Model):
    PRIORITY = (
        ("Urgent", "Urgent"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low")
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField("Completion date")
    is_completed = models.BooleanField("Completed")
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY,
        default="Urgent"
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="task"
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks"
    )

    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return (f"{self.name}"
                f"(task_type: {self.task_type.name},"
                f"completed: {self.is_completed})"
                )

    def get_absolute_url(self):
        return reverse("task:task-detail", kwargs={"pk": self.pk})


class Team(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(
        Worker,
        related_name="team"
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = (
        ("Work", "Work"),
        ("Finished", "Finished"),
        ("Canceled", "Canceled")
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Work"
    )
    team = models.ManyToManyField(
        Team,
        related_name="project"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("task:project-detail", kwargs={"pk": self.pk})
