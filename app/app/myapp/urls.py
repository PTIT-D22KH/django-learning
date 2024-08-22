from django.urls import path
from . import views
from . views import my_form_view, success_view, report_view

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('my-form/', my_form_view, name='my_form'),
    path('success/', success_view, name='success'),
    path('report/', report_view, name='report')
]