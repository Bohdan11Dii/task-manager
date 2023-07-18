from django.test import TestCase
from task.models import Position, Task, TaskType
from django.contrib.auth import get_user_model
# Create your tests here.


class ModelTests(TestCase):
    def test_position_str(self):
        position = Position.objects.create(name="test")
        self.assertEqual(str(position), position.name)
    
    def test_worker_str(self):
        worker = get_user_model().objects.create_user(
            username="test",
            password="test12345"
        )
        self.assertEqual(str(worker), worker.username)

    def test_task_str(self):
        task_type = TaskType.objects.create(name="test")
        task = Task.objects.create(
            name="test",
            description="test",
            deadline="2000-12-12",
            task_type=task_type,
            is_completed=True,
            priority="Urgent"
        )

        self.assertEqual(str(task), (f"{task.name}"
                                    f"(task_type: {task_type.name},"
                                    f"completed: {task.is_completed})")
                                    )

    def test_create_worker_witt_position(self):
        username="test"
        password="test12345"
        position = Position.objects.create(name="test")
        worker = get_user_model().objects.create_user(
            username=username,
            password=password,
            position=position
        )
        self.assertEqual(worker.username, username)
        self.assertTrue(worker.check_password(password))
        self.assertEqual(worker.position, position)
