from rest_framework import routers
from .views import CheckPointViewSet, CommentTaskViewSet, TaskViewSet, TaskFilesViewSet, SubTaskViewSet


router = routers.DefaultRouter()


router.register('check_point', CheckPointViewSet)
router.register('comment_task', CommentTaskViewSet)
router.register('sub_task', SubTaskViewSet)
router.register('task', TaskViewSet)
router.register('task_files', TaskFilesViewSet)


urlpatterns = router.urls
