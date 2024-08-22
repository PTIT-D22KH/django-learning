# # /app/authentication/tests/test_views.py
# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User

# class RegistrationViewTests(TestCase):
#     def setUp(self):
#         """Set up a client for testing."""
#         self.client = Client()

#     def test_registration_view_get_status_code(self):
#         """Test the registration view GET request returns a 200 status code."""
#         response = self.client.get(reverse('registration'))
#         self.assertEqual(response.status_code, 200)

#     def test_registration_view_get_template(self):
#         """Test the registration view GET request uses the correct template."""
#         response = self.client.get(reverse('registration'))
#         self.assertTemplateUsed(response, 'authentication/register.html')

#     def test_registration_view_post_success(self):
#         """Test the registration view POST request successfully creates a user."""
#         response = self.client.post(reverse('registration'), {
#             'username': 'testuser',
#             'email': 'test@example.com',
#             'password': 'testpass123!'
#         })
#         self.assertEqual(response.status_code, 302)  # Redirect after success
#         self.assertTrue(User.objects.filter(username='testuser').exists())

#     def test_registration_view_post_existing_username(self):
#         """Test the registration view POST request with an existing username."""
#         User.objects.create_user(username='testuser', email='test@example.com', password='testpass123!')
#         response = self.client.post(reverse('registration'), {
#             'username': 'testuser',
#             'email': 'new@example.com',
#             'password': 'testpass123!'
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "User name already exists")

#     def test_registration_view_post_existing_email(self):
#         """Test the registration view POST request with an existing email."""
#         User.objects.create_user(username='testuser', email='test@example.com', password='testpass123!')
#         response = self.client.post(reverse('registration'), {
#             'username': 'newuser',
#             'email': 'test@example.com',
#             'password': 'testpass123!'
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Email already exists")

#     def test_registration_view_post_short_password(self):
#         """Test the registration view POST request with a short password."""
#         response = self.client.post(reverse('registration'), {
#             'username': 'testuser',
#             'email': 'test@example.com',
#             'password': 'short'
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Password should be 8 characters long")