from django.contrib import admin
from django.urls import path, re_path
from django.urls import include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from user_api.views import DecoratedTokenObtainPairView, DecoratedTokenVerifyView, DecoratedTokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="User API",
        default_version='v1',
        description="",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=False,
    permission_classes=(permissions.IsAuthenticated,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('user_api.urls', 'user_api'), namespace='user_api')),
    path('api/auth/sign_in/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/sign_in/refresh/', DecoratedTokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/sign_in/verify/', DecoratedTokenVerifyView.as_view(), name='token_verify'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

