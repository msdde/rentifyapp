from django.test import TestCase
from django.urls import reverse

from rentify.vanilla.mixins import CreateUserForTestMixin


class BrandsCreateViewTests(TestCase, CreateUserForTestMixin):

    # test if the user is not staff and manually input the brand-create url should return forbidden 403
    def test_get_create_when_logged_in_user_is_not_staff_expect_403_forbidden(self):
        self._create_user(is_staff=False)
        self.client.login(**self.USER_DATA)

        response = self.client.get(reverse("brand-create"))
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, "403.html")

    # test if the user is staff and create brand the status code should be 200
    def test_get_create_when_logged_in_user_is_staff_expect_success(self):
        self._create_user(is_staff=True)
        self.client.login(**self.USER_DATA)

        response = self.client.get(reverse("brand-create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "brands/brand-create.html")

    # test if after successful created brand if django redirects to brands-list
    def test_post_create_redirect_to_brands_list(self):
        self._create_user(is_staff=True)
        self.client.login(**self.USER_DATA)

        brand_data = {
            "name": "TestBrand",
            "slug": "test-slug-112233",
        }

        response = self.client.post(reverse("brand-create"), data=brand_data, follow=True)

        self.assertRedirects(response, reverse("brands-list"))
