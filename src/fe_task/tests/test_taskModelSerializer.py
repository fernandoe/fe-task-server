from django.test import TestCase

from ..serializers import TaskSerializer


class TestTaskModelSerializer(TestCase):
    def setUp(self):
        self.serializer_data = {
            'name': 'serializer name',
            'description': 'some object description'
        }

    def test_is_valid(self):
        serializer = TaskSerializer(data=self.serializer_data)
        assert serializer.is_valid()
