from django.views.generic import TemplateView
from rentify.accounts.models import RentifyProfile
from rentify.bookings.models import Booking
from rentify.brands.models import Brand
from rentify.cars.models import Cars
from rentify.categories.models import Category
from rentify.reviews.models import Review


class IndexView(TemplateView):
    template_name = "vanilla/index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        # Get last 3 reviews
        context["reviews"] = Review.objects.all().order_by('-id')[:3]
        context["cars"] = Cars.objects.all().order_by('-id')[:3]
        # Get the counts for every app
        context["review_count"] = Review.objects.all().count()
        context["profiles_count"] = RentifyProfile.objects.all().count()
        context["cars_count"] = Cars.objects.all().count()
        context["categories_count"] = Category.objects.all().count()
        context["brands_count"] = Brand.objects.all().count()
        context["bookings_count"] = Booking.objects.all().count()

        return context
