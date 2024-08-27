from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['username', 'company_name', 'email', 'is_staff', 'is_client', 'is_service_company', 'is_manager']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('company_name', 'is_client', 'is_service_company', 'is_manager')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('company_name', 'is_client', 'is_service_company', 'is_manager')}),
    )
    list_filter = ['is_staff', 'is_client', 'is_service_company', 'is_manager', 'is_active']


admin.site.register(User, CustomUserAdmin)
