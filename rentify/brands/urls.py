from django.urls import include, path

from rentify.brands.views import BrandsListView, CreateBrandView, EditBrandView, DeleteBrandView
from rentify.cars.views import CarsByBrandListView

urlpatterns = [
    path("", BrandsListView.as_view(), name="brands-list"),
    path("create/", CreateBrandView.as_view(), name="brand-create"),
    path("<slug:slug>/", include([
        path("", CarsByBrandListView.as_view(), name="cars-by-brand"),
        path("edit/", EditBrandView.as_view(), name="brand-edit"),
        path("delete/", DeleteBrandView.as_view(), name="brand-delete"),
        ]),
    )
]
