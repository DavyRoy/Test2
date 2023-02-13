from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from gpg.views import AuthViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="PROXY API",
      default_version='v1',
      description="Proxy api service",
      terms_of_service="",
   ),
   public=True,
   permission_classes=(IsAuthenticated,),
)

router = routers.DefaultRouter()
router.register('auth', AuthViewSet, basename='auth')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(('gpg.urls', 'gpg'), namespace='gpg')),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
