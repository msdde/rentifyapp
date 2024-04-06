from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.views import View

UserModel = get_user_model()


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff if hasattr(self, 'request') else False

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied("You do not have permission to access this page.")
        return super().handle_no_permission()


class UserRequestPersonalInfoMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs['pk']:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CreateUserForTestMixin:
    USER_DATA = {
            "email": "TestUser@test.bg",
            "password": "TestPassword",
        }

    def _create_user(self, is_staff=False):
        return UserModel.objects.create_user(**self.USER_DATA, is_staff=is_staff)
