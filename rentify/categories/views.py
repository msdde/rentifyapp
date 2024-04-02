from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rentify.categories.forms import CreateCategoryForm
from rentify.categories.models import Category
from rentify.vanilla.mixins import StaffRequiredMixin


class CreateCategoryView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    template_name = "categories/category-create.html"
    form_class = CreateCategoryForm
    success_url = reverse_lazy("categories-list")


class CategoriesListView(ListView):
    model = Category
    template_name = "categories/categories-list.html"
    context_object_name = "category"


class EditCategoryView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    queryset = Category.objects.all()
    fields = "__all__"
    template_name = "categories/category-edit.html"

    def get_success_url(self):
        return reverse("categories-list",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # list of attributes
        attributes = ["name", "image", "slug", "description", "image"]
        # populate the context with object attributes
        context.update({attr: getattr(self.object, attr) for attr in attributes})
        return context


class DeleteCategoryView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Category
    template_name = "categories/category-delete.html"
    success_url = reverse_lazy("categories-list")
