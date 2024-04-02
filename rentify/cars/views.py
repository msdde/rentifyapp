from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, TemplateView

from rentify.bookings.forms import CarBookingForm
from rentify.brands.models import Brand
from rentify.cars.forms import CreateCarForm
from rentify.cars.mixins import SlugMixin
from rentify.cars.models import Cars
from rentify.categories.models import Category
from rentify.vanilla.mixins import StaffRequiredMixin


class CreateCarView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    template_name = "cars/car-create.html"
    form_class = CreateCarForm
    success_url = reverse_lazy("cars/cars-list.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data
        context["year"] = 2020
        context["categories"] = Category.objects.all()
        context["brands"] = Brand.objects.all()
        return context

    def get_success_url(self):
        return reverse("cars-list",)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CarsListView(ListView):
    queryset = Cars.objects.all()
    template_name = "cars/cars-list.html"


class EditCarView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    queryset = Cars.objects.all()
    fields = "__all__"
    template_name = "cars/car-edit.html"

    def get_success_url(self):
        return reverse("cars-list",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # list of attributes
        attributes = ["brand", "model", "year", "price", "image", "gearbox", "slug", "category"]
        # populate the context with object attributes
        context.update({attr: getattr(self.object, attr) for attr in attributes})
        context["categories"] = Category.objects.all()
        context["brands"] = Brand.objects.all()
        context["car"] = self.object
        return context


class DeleteCarView(LoginRequiredMixin, StaffRequiredMixin, SlugMixin, DeleteView):
    model = Cars
    template_name = "cars/car-delete.html"
    success_url = reverse_lazy("cars-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = Cars.objects.get(slug=self.get_slug())  # Fetching the category object
        context['car'] = car
        return context


class CarsByCategoriesListView(SlugMixin, ListView):
    template_name = "cars/cars-by-categories.html"
    context_object_name = 'cars_list'
    model = Cars

    # Moved to mixins.py
    # separate function to get the slug and use it further
    # def get_slug(self):
    #     slug = self.kwargs['slug']
    #     return slug

    # fetching the category name based on the slug in url
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.get_slug())  # Fetching the category object
        context['category'] = category
        return context

    def get_queryset(self):
        category = Category.objects.get(slug=self.get_slug())
        queryset = Cars.objects.filter(category=category)
        return queryset


class CarsByBrandListView(SlugMixin, ListView):
    template_name = "cars/cars-by-brand.html"
    context_object_name = 'cars_list'
    model = Cars

    # fetching the category name based on the slug in url
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = Brand.objects.get(slug=self.get_slug())  # Fetching the category object
        context['brand'] = brand
        return context

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.get_slug())
        queryset = Cars.objects.filter(brand=brand)
        return queryset
