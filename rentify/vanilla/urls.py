from django.urls import path
from rentify.vanilla.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index")
]
