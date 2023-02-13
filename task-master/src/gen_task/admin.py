from django.contrib import admin
from .models import CheckPoint, CommentTask, Task, TaskFile, SubTask, TaskAnalyticData


@admin.register(CheckPoint)
class CheckPointAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'project',
                    'priority',
                    'status')


@admin.register(CommentTask)
class CommentTaskAdmin(admin.ModelAdmin):
    list_display = ('created_by',
                    'text')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'check_point',
                    'priority',
                    'status',
                    'type')


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'task',
                    'is_completed')


@admin.register(TaskFile)
class TaskFilesAdmin(admin.ModelAdmin):
    list_display = ('created_by',
                    'file_id')


@admin.register(TaskAnalyticData)
class TaskAnalyticDataAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'task',
                    'created',
                    'processing',
                    'on_pause',
                    'on_review',
                    'returned',
                    'agreed',
                    'finished'
                    ]
