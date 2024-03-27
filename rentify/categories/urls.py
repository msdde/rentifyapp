from django.urls import path, include

from rentify.cars.views import CarsByCategoriesListView
from rentify.categories.views import CategoriesListView, CreateCategoryView, EditCategoryView, DeleteCategoryView

urlpatterns = [
    path("", CategoriesListView.as_view(), name="categories-list"),
    path("create/", CreateCategoryView.as_view(), name="category-create"),
    path("<slug:slug>/", include([
        path("", CarsByCategoriesListView.as_view(), name="cars-by-categories"),
        path("edit/", EditCategoryView.as_view(), name="category-edit"),
        path("delete/", DeleteCategoryView.as_view(), name="category-delete"),
        ]),
    )
]

