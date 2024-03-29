from django.views.generic import TemplateView

from rentify.reviews.models import Review


class IndexView(TemplateView):
    template_name = "vanilla/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the count of reviews for the current user's profile
        context['reviews_count'] = Review.objects.all().count()
        return context
