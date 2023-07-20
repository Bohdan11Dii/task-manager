from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from task.models import Position


POSITION_URL = reverse("task:position-list")
WORKER_URL = reverse("task:worker-create")


class PublicPositionTests(TestCase):
    def test_login_required(self):
        response = self.client.get(POSITION_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivatePositionTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_position(self):
        Position.objects.create(
            name="test",
        )
        Position.objects.create(
            name="test1",
        )

        response = self.client.get(POSITION_URL)

        position = Position.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["position_list"]),
            list(position)
        )
        self.assertTemplateUsed(
            response,
            "task/position_list.html"
        )


class PublicWorkerTests(TestCase):
    def test_login_required(self):
        response = self.client.get(WORKER_URL)

        self.assertNotEqual(response.status_code, 200)
