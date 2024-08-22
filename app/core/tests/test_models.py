"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import Items
import datetime


class ModelTests(TestCase):
    """Test models."""
    
    
    def setUp(self):
        """Set up a user for testing."""
        self.user = get_user_model().objects.create_user(
            email = 'test@example.com',
            password='testpass123!'
        )
    
    def test_create_items_with_details_successful(self):
        """Test creating a user with an detail is successful."""
        date = datetime.date(2024, 8, 22)
        description = 'My first task to do'
        owner = self.user,
        status = False,
        category = 'Test Category'
        
        item = Items.objects.create(
            date = date,
            description = description,
            owner = owner,
            status = status,
            category = category
        )
        
        self.assertEqual(item.date, date)
        self.assertEqual(item.description, description)
        self.assertEqual(item.owner, self.user)
        self.assertFalse(item.status)
        self.assertEqual(item.category, category)