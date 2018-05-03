from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        read_only_fields = ('uuid',)
        fields = ('uuid', 'created_at', 'updated_at', 'name', 'parent', 'description',)
