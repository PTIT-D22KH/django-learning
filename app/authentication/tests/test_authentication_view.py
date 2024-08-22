# /app/authentication/tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse

class RegistrationViewTests(TestCase):
    def setUp(self):
        """Set up a client for testing."""
        self.client = Client()

    def test_registration_view_get_status_code(self):
        """Test the registration view GET request returns a 200 status code."""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_registration_view_get_template(self):
        """Test the registration view GET request uses the correct template."""
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'authentication/register.html')