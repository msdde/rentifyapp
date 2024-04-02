from django.urls import path
from rentify.bookings.views import BookingInvoiceView, CarBookingView

urlpatterns = [
    path("<slug:slug>", CarBookingView.as_view(), name="car-booking"),
    path("<int:pk>/", BookingInvoiceView.as_view(), name="booking-invoice"),
]
