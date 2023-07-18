from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from task.models import Position


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        position = Position.objects.create(name="test")
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345"
        )
        self.client.force_login(self.admin_user)
        self.worker = get_user_model().objects.create_user(
            username="worker",
            password="worker12345",
            position=position
        )

    def test_worker_position_listed(self):
        """Tests that worker's position
        is in list_display on worker admin page"""
        url = reverse("admin:task_worker_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.worker.position)

    def test_worker_detailed_position_listed(self):
        """Tests that worker's position is on worker detail admin page"""
        url = reverse("admin:task_worker_change", args=[self.worker.id])
        response = self.client.get(url)

        self.assertContains(response, self.worker.position)