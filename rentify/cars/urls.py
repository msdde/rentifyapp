from django.urls import path, include

from rentify.cars.views import CreateCarView, EditCarView, DeleteCarView, CarsListView

urlpatterns = [
    path("", CarsListView.as_view(), name="cars-list"),
    path("create/", CreateCarView.as_view(), name="car-create"),
    path("<slug:slug>/", include([
        path("edit/", EditCarView.as_view(), name="car-edit"),
        path("delete/", DeleteCarView.as_view(), name="car-delete"),
        ]),
     )
]
