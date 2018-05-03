import uuid

from django.urls import reverse
from fe_core.factories import UserFactory, EntityFactory
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from ..models import Task

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

EXAMPLE_DATA = {
    'name': 'exmaple name',
    'description': 'some exmaple description'
}


class TestTaskModelViewSet(APITestCase):

    def setUp(self):
        self.entity = EntityFactory()
        self.user = UserFactory(entity=self.entity)
        payload = jwt_payload_handler(self.user)
        user_token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token)

    def test_response_201(self):
        response = self.client.post(reverse('task-list'), EXAMPLE_DATA)
        assert status.HTTP_201_CREATED == response.status_code
        task = Task.objects.first()
        data = response.data
        assert 6 == len(data)
        assert str(task.uuid) == data['uuid']
        assert task.name == data['name']
        assert task.description == data['description']
        assert task.entity == self.entity
        assert task.user == self.user
        assert task.parent is None

    def test_anonymous_user(self):
        self.client.logout()
        response = self.client.post(reverse('task-list'), EXAMPLE_DATA)
        assert status.HTTP_403_FORBIDDEN == response.status_code

    def test_create_field_with_parent(self):
        data = EXAMPLE_DATA.copy()
        parent_uuid = str(uuid.uuid4())
        data['parent'] = parent_uuid
        response = self.client.post(reverse('task-list'), data)
        assert response.data['parent'] == parent_uuid
