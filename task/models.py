import datetime
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.


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
        return f"{self.username} ({self.position.name})"


class Task(models.Model):
    PRIORITY = (
        ("u", "Urgent"),
        ("h", "High"),
        ("m", "Medium"),
        ("l", "Low")
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField("Completion date", default=timezone.now())
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=10, choices=PRIORITY, default="u")
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="task"
    )
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tasks")


    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return (f"{self.name} "
                f"(task_type: {self.task_type.name},"
                f"completed: {self.is_completed})"
                )
