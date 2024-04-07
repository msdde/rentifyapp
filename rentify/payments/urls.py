from django.urls import path
from rentify.payments.views import CreateCheckOutSessionView, payment_success, payment_cancel

urlpatterns = [
    path("checkout/<int:pk>/", CreateCheckOutSessionView.as_view(), name="checkout"),
    path("success/", payment_success, name="payment-success"),
    path("cancel/", payment_cancel, name="payment-cancel"),
]
