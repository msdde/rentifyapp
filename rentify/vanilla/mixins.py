from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff if hasattr(self, 'request') else False

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied("You do not have permission to access this page.")
        return super().handle_no_permission()
