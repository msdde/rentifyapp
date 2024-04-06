from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rentify.vanilla.mixins import CreateUserForTestMixin

UserModel = get_user_model()


class CategoriesCreateViewTests(TestCase, CreateUserForTestMixin):

    # test if the user is not staff and manually input the category-create url should return forbidden 403
    def test_get_create_when_logged_in_user_is_not_staff_expect_403_forbidden(self):
        self._create_user(is_staff=False)
        self.client.login(**self.USER_DATA)

        response = self.client.get(reverse("category-create"))
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, "403.html")

    # test if the user is staff and create category the status code should be 200
    def test_get_create_when_logged_in_user_is_staff_expect_success(self):
        self._create_user(is_staff=True)
        self.client.login(**self.USER_DATA)

        response = self.client.get(reverse("category-create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "categories/category-create.html")

    # test if after successful created category if django redirects to categories-list
    def test_post_create_redirect_to_categories_list(self):
        self._create_user(is_staff=True)
        self.client.login(**self.USER_DATA)

        category_data = {
            "name": "Audi",
            "slug": "test-slug-123",
            "description": "Test description"
        }

        response = self.client.post(reverse("category-create"), data=category_data, follow=True)

        self.assertRedirects(response, reverse("categories-list"))
