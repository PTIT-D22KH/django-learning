"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""
    
    
    def create_task_with_detail_successful(self):
        """Test creating a task with detail successful"""
        user = 'duongvct'
        title = 'My first task'
        description = 'My first task to test the system'
        is_completed = False
        create = '08/22/2024'
        
        task = get_user_model().objects.create_task(
            user = user,
            title = title,
            description = description,
            is_completed = is_completed,
            create = create
        )
        
        self.assertEqual(task .user, user)
        self.assertEqual(task .title, title)
        self.assertEqual(task .description, description)
        self.assertFalse(task.is_completed)
        # self.assertEqual(user.user, user)