from django.test import TestCase

from task.forms import (
    WorkerCreationForm,
    TaskTypeSearchForm,
    TaskSearchForm,
    PositionSearchForm,
)
from task.models import Position


class FormsTests(TestCase):
    def test_worker_creation_form_is_valid(self):
        position = Position.objects.create(name="test")
        form_data = {
            "username": "new_user",
            "password1": "user12345",
            "password2": "user12345",
            "first_name": "Test first",
            "last_name": "Test last",
            "position": position
        }

        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_type_search_form(self):
        form_data = {
            "name": "test"
        }
        form = TaskTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_search_form(self):
        form_data = {
            "name": "test"
        }
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_position_search_form(self):
        form_data = {
            "name": "test"
        }
        form = PositionSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
