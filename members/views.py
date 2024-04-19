from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet

from .models import Members, Organizations
from .serializers import MembersSerializer, OrganizationsSerializer


class CheckPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_staff


class MembersViewSet(ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    permission_classes = [CheckPermission]


class OrganizationsViewSet(ModelViewSet):
    queryset = Organizations.objects.all()
    serializer_class = OrganizationsSerializer
    permission_classes = [CheckPermission]
