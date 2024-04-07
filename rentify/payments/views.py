import stripe
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View

from rentify.bookings.models import Booking
from rentify.settings import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


class CreateCheckOutSessionView(View):

    def post(self, request, *args, **kwargs):

        booking = Booking.objects.get(pk=self.kwargs["pk"])
        host = self.request.get_host()

        duration = (booking.end_date - booking.start_date).days + 1
        # Calculate total price
        total_price = duration * booking.booked_car.price

        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f"{booking.booked_car.brand.name} {booking.booked_car.model}",
                    },
                    'unit_amount': total_price * 100,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url="http://{}{}".format(host, reverse("payment-success")),
            cancel_url="http://{}{}".format(host, reverse("payment-cancel")),
        )

        return redirect(checkout_session.url, code=303)


def payment_success(request):
    return render(request, "payments/payment-success.html")


def payment_cancel(request):
    return render(request, "payments/payment-cancel.html")

#                 4242 4242 4242 4242