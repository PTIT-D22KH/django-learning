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
            username = 'testuser',
            email = 'test@example.com',
            password='testpass123!'
        )
    
    def test_create_items_with_details_successful(self):
        """Test creating a user with an detail is successful."""
        date = datetime.date(2024, 8, 22)
        description = 'My first task to do'
        owner = self.user
        status = False
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
        
    
    def test_formatted_date(self):
        """Test the formatted_date method"""
        item = Items.objects.create(
            date = datetime.date(2024, 8, 22),
            description = 'Test',
            owner = self.user,
            status = False,
            category = 'Test Category'
        )
        self.assertEqual(item.get_formatted_data(), '2024/08/22')
        
        item_no_date = Items.objects.create(
            description = 'Test',
            owner = self.user,
            status = False,
            category = 'Test Category'
        )
        self.assertIsNone(item_no_date.get_formatted_data())
        
        
    def test_items_to_string(self):
        """Test __str__ method of items."""
        item = Items.objects.create(
            date = datetime.date(2024, 8, 22),
            description = 'Test',
            owner = self.user,
            status = False,
            category = 'Test Category'
        )
        print(str(item))
        expected_string = f"{self.user} {item.get_formatted_data()} {item.description[:50]} {item.category}"
        self.assertEqual(str(item), expected_string)
        
        
    def test_items_ordering(self):
        """Test items ordering by date"""
        item1 = Items.objects.create(
            date = datetime.date(2024, 8, 22),
            description = 'Test 1',
            owner = self.user,
            status = False,
            category = 'Test1 Category'
        )
        item2 = Items.objects.create(
            date = datetime.date(2024, 8, 23),
            description = 'Test 2',
            owner = self.user,
            status = False,
            category = 'Test2 Category'
        )
        
        items = Items.objects.all()
        self.assertEqual(items[0], item2)
        self.assertEqual(items[1], item1)
