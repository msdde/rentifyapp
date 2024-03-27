from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rentify import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("rentify.vanilla.urls")),
    path("accounts/", include("rentify.accounts.urls")),
    path("cars/", include("rentify.cars.urls")),
    path("categories/", include("rentify.categories.urls"))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
