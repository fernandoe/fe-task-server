from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('get_uuid', 'created_at', 'updated_at', 'user', 'entity', 'name', 'parent', 'description')
