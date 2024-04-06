from django.urls import path
from rentify.mail.views import ContactFormView, SuccessMessageView

urlpatterns = [
    path("", ContactFormView.as_view(), name="contact"),
    path("success/", SuccessMessageView.as_view(), name="message-sent")
]
