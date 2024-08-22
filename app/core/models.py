from django.db import models
from django.contrib.auth.models import User, BaseUserManager


class TaskManager(models.Manager):
    """Manager for tasks."""

    def create_task(self, user, title=None, description=None, is_completed=False, create=None, **extra_fields):
        """Create, save and return a new task."""
        if not user:
            raise ValueError("Task must be assigned to a user.")
        task = self.model(
            user=user,
            title=title,
            description=description,
            is_completed=is_completed,
            create=create,
            **extra_fields
        )
        task.save(using=self._db)
        return task


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    create = models.DateTimeField()

    objects = TaskManager()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['is_completed']