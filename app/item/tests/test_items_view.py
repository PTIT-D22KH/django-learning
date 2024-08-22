from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import Items, Category
import datetime
import json


class ViewTests(TestCase):
    def setUp(self):
        """Set up a user and client for testing."""
        self.client = Client()
        username = 'testuser'
        email = 'test@example.com'
        password = 'testpassword123!'
        self.user = get_user_model().objects.create_user(
            username = username,
            email = email,
            password = password,
        )
        self.client.login(
            username = 'testuser',
            password = password
        )
        category_name = 'Test Category'
        item_owner = self.user
        item_date = datetime.date(2024, 8, 22)
        item_category = category_name
        item_description = 'Test description'
        self.category = Category.objects.create(
            name = category_name
        )
        self.item = Items.objects.create(
            owner = item_owner,
            date = item_date,
            category = item_category,
            description = item_description
        )
        
    def test_index_view(self):
        """Test the index view."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Items/index.html')
        self.assertContains(response, self.category.name)

        
        