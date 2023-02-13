from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as Admin
from django.utils.translation import gettext, gettext_lazy as _

from .models import Role, User, ProjectGroup

admin.site.register(Role)
admin.site.register(ProjectGroup)


@admin.register(User)
class UserAdmin(Admin):
    fieldsets = (
        (None, {'fields': (
            'username',
            'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'phone',
                'kpi',
                'avatar')}),
        (_('Permissions'), {
            'fields': (
                      'is_active',
                      'is_staff',
                      'is_superuser',
                      'groups',
                      'user_permissions',
                      'role'),
        }),
        (_('Important dates'), {
            'fields': (
                 'last_login',
                 'date_joined',
                 'updated_by',
                 'updated_at',
                 'created_by',
                 'created_at',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'phone', 'role', 'username', 'password1', 'password2'),
        }),
    )

    readonly_fields = ('updated_by', 'updated_at', 'created_by', 'created_at', 'kpi')
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions', 'role')
