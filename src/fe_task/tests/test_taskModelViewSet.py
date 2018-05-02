from django.test import TestCase
from django.urls import reverse
from rest_framework import status

EXAMPLE_DATA = {
    'name': 'exmaple name',
    'description': 'some exmaple description'
}


class TestTaskModelViewSet(TestCase):
    def test_response_201(self):
        response = self.client.post(reverse('task-list'), EXAMPLE_DATA)
        assert status.HTTP_201_CREATED == response.status_code
