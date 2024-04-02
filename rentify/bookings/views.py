from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from rentify.accounts.models import RentifyProfile
from rentify.bookings.forms import CarBookingForm

from rentify.bookings.models import Booking
from rentify.cars.models import Cars
from rentify.vanilla.mixins import UserRequestPersonalInfoMixin


class CarBookingView(LoginRequiredMixin, CreateView):
    template_name = "bookings/car-booking.html"
    form_class = CarBookingForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the car object based on the slug provided in the URL
        context['car'] = get_object_or_404(Cars, slug=self.kwargs['slug'])
        return context

    def get_success_url(self):

        return reverse_lazy("booking-invoice", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.bill_to = self.request.user

        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        car = get_object_or_404(Cars, slug=slug)

        return render(request, self.template_name, {'car': car})


class BookingInvoiceView(LoginRequiredMixin, DetailView):
    template_name = "bookings/booking-invoice.html"
    model = Booking

    # only the user who is sending the request can access his invoice
    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != self.get_object().bill_to.user_profile.pk:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # Fetch the booking object based on the pk parameter in the URL
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        booking = self.object
        context["author"] = RentifyProfile.objects.get(pk=self.request.user.id)
        # Calculate duration
        duration = (booking.end_date - booking.start_date).days + 1
        # Calculate total price
        total_price = duration * booking.booked_car.price

        context['total_price'] = total_price
        return context


class BookingsByUserView(UserRequestPersonalInfoMixin, LoginRequiredMixin, ListView):
    template_name = "accounts/profile-bookings.html"
    model = Booking

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(bill_to=self.kwargs['pk'])

        return queryset
