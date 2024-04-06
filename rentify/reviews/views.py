from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from rentify.accounts.models import RentifyProfile
from rentify.reviews.forms import CreateReviewForm
from rentify.reviews.models import Review
from rentify.vanilla.mixins import UserRequestPersonalInfoMixin


class CreateReviewView(LoginRequiredMixin, CreateView):
    form_class = CreateReviewForm
    template_name = "reviews/review-create.html"
    success_url = reverse_lazy("reviews-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data
        context["author"] = RentifyProfile.objects.get(pk=self.request.user.id)
        return context

    def form_valid(self, form):
        # Assign the user associated with the profile to the author field of the review
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReviewsListView(ListView):
    model = Review
    template_name = "reviews/reviews-list.html"
    context_object_name = "review"

    def get_queryset(self):
        # Newest reviews will be on top
        return Review.objects.order_by("-date")


class DeleteReviewView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = "reviews/review-delete.html"
    success_url = reverse_lazy("reviews-list")

    # prevent user to access the delete form of someone else review, except staff or superuser
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff or not request.user.is_superuser:
            if request.user.pk != self.get_object().author.user_profile.pk:
                raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ReviewsByUserView(UserRequestPersonalInfoMixin, LoginRequiredMixin, ListView):
    template_name = "accounts/profile-reviews.html"
    model = Review

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author_id=self.kwargs['pk'])
        return queryset
