from rest_framework import routers
from .views import ProjectGroupViewSet, RoleViewSet, UserViewSet,  AuthViewSet

router = routers.DefaultRouter()


router.register('user', UserViewSet)
router.register('role', RoleViewSet)
router.register('project_group', ProjectGroupViewSet)

router.register('auth', AuthViewSet)


urlpatterns = router.urls
