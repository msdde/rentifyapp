from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from rentify.accounts.models import RentifyProfile
from rentify.reviews.forms import CreateReviewForm
from rentify.reviews.models import Review


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
        form.save(commit=False)
        form.instance.author = RentifyProfile.objects.get(pk=self.request.user.id)
        form.save()
        return super().form_valid(form)


class ReviewsListView(ListView):
    model = Review
    template_name = "reviews/reviews-list.html"
    context_object_name = "review"


class DeleteReviewView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = "reviews/review-delete.html"
    success_url = reverse_lazy("reviews-list")
