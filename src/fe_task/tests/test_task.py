from django.test import TestCase

from .factories import TaskFactory


class TestTask(TestCase):
    def test_factory(self):
        task = TaskFactory()
        assert task is not None

    def test_field_parent(self):
        task = TaskFactory()
        assert hasattr(task, 'parent')

    def test__str__(self):
        task = TaskFactory(name='test__str__')
        assert 'test__str__' == str(task)
