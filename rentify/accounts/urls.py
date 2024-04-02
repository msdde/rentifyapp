from django.urls import path, include
from rentify.accounts.views import UserLoginView, UserSignUpView, logout_user, ProfileDetailsView, ProfileUpdateView, \
    ProfileDeleteView
from rentify.bookings.views import BookingsByUserView
from rentify.reviews.views import ReviewsByUserView

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("signup/", UserSignUpView.as_view(), name="signup"),
    path("logout/", logout_user, name="logout"),
    path(
        "profile/<int:pk>/", include([
            path("", ProfileDetailsView.as_view(), name="profile-details"),
            path("reviews/", ReviewsByUserView.as_view(), name="profile-reviews"),
            path("bookings/", BookingsByUserView.as_view(), name="profile-bookings"),
            path("edit/", ProfileUpdateView.as_view(), name="profile-edit"),
            path("delete/", ProfileDeleteView.as_view(), name="profile-delete")
        ]),
    )
]

