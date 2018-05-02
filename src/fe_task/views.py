from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        user = self.request.user
        entity = user.entity
        serializer.save(user=user, entity=entity)
