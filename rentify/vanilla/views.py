from django.shortcuts import render
from django.views.generic import TemplateView

from rentify.vanilla.utils import get_counts


class IndexView(TemplateView):
    template_name = "vanilla/index.html"


def counts_view(request):
    profile_count, car_count, brand_count, category_count = get_counts()

    context = {
        'car_count': car_count,
        'brand_count': brand_count,
        'category_count': category_count,
    }
    return render(request, "vanilla/index.html", context)
