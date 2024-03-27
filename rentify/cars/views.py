from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from rentify.cars.forms import CreateCarForm
from rentify.cars.models import Cars
from rentify.categories.models import Category


class CreateCarView(LoginRequiredMixin, CreateView):
    template_name = "cars/car-create.html"
    form_class = CreateCarForm
    success_url = reverse_lazy("cars/cars-list.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data
        context["year"] = 2020
        context["categories"] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse("cars-list",)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CarsListView(ListView):
    queryset = Cars.objects.all()
    template_name = "cars/cars-list.html"


class EditCarView(LoginRequiredMixin, UpdateView):
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
        context["car"] = self.object
        return context


class DeleteCarView(LoginRequiredMixin, DeleteView):
    model = Cars
    template_name = "cars/car-delete.html"
    success_url = reverse_lazy("cars-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        car = Cars.objects.get(slug=slug)  # Fetching the category object
        context['car'] = car
        return context


class CarsByCategoriesListView(ListView):
    template_name = "cars/cars-by-categories.html"
    context_object_name = 'cars_list'
    model = Cars

    # fetching the category name based on the slug in url
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)  # Fetching the category object
        context['category'] = category
        return context

    def get_queryset(self):
        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)
        queryset = Cars.objects.filter(category=category)
        return queryset

