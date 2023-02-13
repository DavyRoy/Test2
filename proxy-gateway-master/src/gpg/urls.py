from rest_framework import routers

from .views import (
    CheckPointViewSet, CommentTaskViewSet, ProjectGroupViewSet, SubTaskViewSet, TaskFileViewSet, TaskViewSet,
    UserViewSet
)

router = routers.DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('project_group', ProjectGroupViewSet, basename='project_group')

router.register('task', TaskViewSet, basename='task')
router.register('check_point', CheckPointViewSet, basename='check_point')
router.register('comment_task', CommentTaskViewSet, basename='comment_task')
router.register('sub_task', SubTaskViewSet, basename='sub_task')
router.register('task_file', TaskFileViewSet, basename='task_file')


urlpatterns = router.urls
