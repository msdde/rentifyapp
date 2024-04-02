from django.urls import path, include

from rentify.reviews.views import CreateReviewView, ReviewsListView, DeleteReviewView, ReviewsByUserView

urlpatterns = [
    path("", ReviewsListView.as_view(), name="reviews-list"),
    path("create/", CreateReviewView.as_view(), name="review-create"),
    path(
        "<int:pk>/", include([
            path("delete/", DeleteReviewView.as_view(), name="review-delete")
        ]),
    )
]
