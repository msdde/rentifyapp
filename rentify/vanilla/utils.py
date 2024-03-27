from rentify.accounts.models import RentifyProfile
from rentify.brands.models import Brand
from rentify.cars.models import Cars
from rentify.categories.models import Category


def get_counts():
    profile_count = RentifyProfile.objects.all().count()
    car_count = Cars.objects.all().count()
    brand_count = Brand.objects.all().count()
    category_count = Category.objects.all().count()
    return car_count, brand_count, category_count, profile_count
