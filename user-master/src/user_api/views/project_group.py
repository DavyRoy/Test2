from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from user_api.models import ProjectGroup
from user_api.serializers import ProjectGroupSerializer


class ProjectGroupViewSet(ModelViewSet):

    serializer_class = ProjectGroupSerializer
    queryset = ProjectGroup.objects.all()
    permission_classes = [IsAuthenticated]
