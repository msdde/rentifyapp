from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.core.mail import EmailMessage
from rentify.accounts.models import RentifyProfile
from rentify.mail.forms import ContactForm


class ContactFormView(LoginRequiredMixin, FormView):
    form_class = ContactForm
    template_name = "mail/contact.html"
    success_url = reverse_lazy("message-sent")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data
        context["sender"] = RentifyProfile.objects.get(pk=self.request.user.id)
        return context

    def form_valid(self, form):
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        sender = form.cleaned_data["email"]
        subject = form.cleaned_data["subject"]
        message = f"You have a new mail from {first_name} {last_name}\n\n{form.cleaned_data['message']}"

        email = EmailMessage(
            subject,
            message,
            to=["djangorentify@abv.bg"],
            from_email=sender
        )

        email.send()

        return super().form_valid(form)

    def get_form_kwargs(self):
        # Override get_form_kwargs to remove the 'instance' argument
        # since I don't need a model for this form
        kwargs = super().get_form_kwargs()
        kwargs.pop('instance', None)
        return kwargs


class SuccessMessageView(LoginRequiredMixin, TemplateView):
    template_name = "mail/message-sent.html"
