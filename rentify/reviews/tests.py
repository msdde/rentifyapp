from django.test import TestCase
from django.urls import reverse
from rentify.vanilla.mixins import CreateUserForTestMixin


class ReviewCreateViewTests(TestCase, CreateUserForTestMixin):

    # test if the user is not logged the review-create url should return login page
    def test_get_create_review_when_user_is_not_logged_in_redirect_login_page(self):

        response = self.client.get(reverse("review-create"))
        self.assertRedirects(response, reverse("login") + '?next=/reviews/create/')

    # test if after review is submitted user should be redirected to reviews-list url
    def test_post_create_review_redirect_to_reviews_list(self):
        self._create_user(is_staff=False)
        user = self.client.login(**self.USER_DATA)

        review_data = {
            "text": "TestText",
            "author": user
        }

        response = self.client.post(reverse("review-create"), data=review_data)

        self.assertRedirects(response, reverse("reviews-list"))
