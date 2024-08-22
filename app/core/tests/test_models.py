from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime
from core.models import Task  # Replace 'core' with the actual app name


class ModelTests(TestCase):
    """Test models."""
    
    def test_create_task_with_detail_successful(self):
        """Test creating a task with detail successful"""
        user = get_user_model().objects.create_user(
            username='duongvct',
            password='testpass123'
        )
        title = 'My first task'
        description = 'My first task to test the system'
        is_completed = False
        create = datetime.strptime('08/22/2024', '%m/%d/%Y')
        
        task = Task.objects.create_task(
            user=user,
            title=title,
            description=description,
            is_completed=is_completed,
            create=create
        )
        
        self.assertEqual(task.user, user)
        self.assertEqual(task.title, title)
        self.assertEqual(task.description, description)
        self.assertFalse(task.is_completed)
        self.assertEqual(task.create, create)