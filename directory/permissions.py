from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth import get_user_model

User = get_user_model()

class SuperUserPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser
