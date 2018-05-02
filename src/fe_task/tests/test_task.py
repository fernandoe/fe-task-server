from django.test import TestCase

from .factories import TaskFactory


class TestTask(TestCase):
    def test_factory(self):
        task = TaskFactory()
        assert task is not None
