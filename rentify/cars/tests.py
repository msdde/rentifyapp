from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rentify.brands.models import Brand
from rentify.cars.models import Cars
from rentify.categories.models import Category

UserModel = get_user_model()


class CarsCreateViewTests(TestCase):
    USER_DATA = {
        "email": "TestUser@test.bg",
        "password": "TestPassword",
    }

    def _create_user(self, is_staff=False):
        return UserModel.objects.create_user(**self.USER_DATA, is_staff=is_staff)

    # test if the user is not staff and manually input the car-create url should return forbidden 403
    def test_get_create_when_logged_in_user_is_not_staff_expect_403_forbidden(self):
        self._create_user(is_staff=False)
        self.client.login(**self.USER_DATA)

        response = self.client.get(reverse("car-create"))

        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, "403.html")

    # test if the user is staff and create car the status code should be 200
    def test_get_create_when_logged_in_user_is_staff_expect_success(self):
        self._create_user(is_staff=True)
        self.client.login(**self.USER_DATA)

        response = self.client.get(reverse("car-create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cars/car-create.html")


