from django.urls import path, include
from rest_framework import routers

from .views import MembersViewSet, OrganizationsViewSet

router = routers.DefaultRouter()
router.register(r'members', MembersViewSet)
router.register(r'organizations', OrganizationsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
