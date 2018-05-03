from django.test import TestCase

from ..serializers import TaskSerializer


class TestTaskModelSerializer(TestCase):
    def setUp(self):
        self.serializer_data = {
            'name': 'serializer name',
            'description': 'some object description'
        }

    def test_data(self):
        serializer = TaskSerializer(data=self.serializer_data)
        serializer.is_valid()
        data = serializer.data
        assert set(data.keys()) == set(['name', 'parent', 'description'])

    def test_is_valid(self):
        serializer = TaskSerializer(data=self.serializer_data)
        assert serializer.is_valid()
