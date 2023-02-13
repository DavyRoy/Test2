from rest_framework import routers
from .views import DocumentViewSet, TypeDocumentViewSet


router = routers.DefaultRouter()


router.register('document', DocumentViewSet)
router.register('type_document', TypeDocumentViewSet)


urlpatterns = router.urls
