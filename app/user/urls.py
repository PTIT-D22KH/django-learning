"""
URL mappings for the user API.
"""
from django.urls import path
from .views import TaskList
from django.contrib.auth.views import LogoutView

app_name = 'user'

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('logout/', LogoutView.as_view(next_page='user:login'), name='logout'),
]