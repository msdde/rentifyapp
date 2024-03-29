from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from rentify.accounts.forms import RentifyUserCreationForm, LoginForm, ProfileEditForm
from rentify.accounts.models import RentifyProfile
from rentify.brands.models import Brand
from rentify.cars.models import Cars
from rentify.categories.models import Category
from rentify.reviews.models import Review

UserModel = get_user_model()


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = LoginForm
    redirect_authenticated_user = True


class UserSignUpView(CreateView):
    template_name = "accounts/signup.html"
    form_class = RentifyUserCreationForm
    success_url = reverse_lazy("index")
    user = UserModel

    def form_valid(self, form):
        result = super().form_valid(form)

        profile_data = {
            'user': form.instance
        }
        RentifyProfile.objects.create(**profile_data)

        login(self.request, form.instance)

        return result


def logout_user(request):
    logout(request)
    return redirect("index")


class Categories:
    pass


class ProfileDetailsView(DetailView):
    queryset = RentifyProfile.objects.all()
    template_name = "accounts/profile-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the count of reviews for the current user's profile
        context["review_count"] = Review.objects.filter(author=self.object).count()
        context["profiles_count"] = RentifyProfile.objects.all().count()
        context["cars_count"] = Cars.objects.all().count()
        context["categories_count"] = Category.objects.all().count()
        context["brands_count"] = Brand.objects.all().count()

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    queryset = RentifyProfile.objects.all()
    template_name = "accounts/profile-edit.html"
    # fields = ["first_name", "last_name", "city", "country", "profile_picture", "phone_number"]
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse("profile-details", kwargs={
            "pk": self.object.pk,
        })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = "accounts/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())


def profile_count(request):
    profiles_count = RentifyProfile.objects.all().count()
    context = {
        "profiles_count": profiles_count
    }

    return render(request, "vanilla/index.html", context)
