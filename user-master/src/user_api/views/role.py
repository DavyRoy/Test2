from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from user_api.models import Role
from user_api.serializers import RoleSerializer


class RoleViewSet(ModelViewSet):

    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = [IsAuthenticated]
