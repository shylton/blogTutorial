from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_home_page(self):
        """home page load success"""

        response = self.client.get(reverse('blogTutorial:blog_home'))
        self.assertEqual(response.status_code, 200)


class AboutPageTests(TestCase):
    def test_about_page(self):
        """home page load success"""

        response = self.client.get(reverse('blogTutorial:blog_about'))
        self.assertEqual(response.status_code, 200)
