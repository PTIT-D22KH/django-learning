from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = [
        "username",
        'email',
        'age',
        'is_staff',
        'job',
    ]
    list_filter = [
        'is_staff',
    ]
    search_fields = [
        'username',
        'email',
        'age',
    ]
    ordering = ['username',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'job')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age','job')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)