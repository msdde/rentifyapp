from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.views import View


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
