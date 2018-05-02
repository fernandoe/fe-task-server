from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer
from fe_core.factories import UserFactory, EntityFactory


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        user = UserFactory()
        entity = EntityFactory()
        serializer.save(user=user, entity=entity)
