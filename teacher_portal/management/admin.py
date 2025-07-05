from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student

# Importing the custom user model
from django.contrib.auth import get_user_model
MyUser = get_user_model()


admin.site.site_header = "tailwebs."
admin.site.site_title = "tailwebs."
admin.site.index_title = "Welcome to the tailwebs admin dashboard"

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'role', 'is_staff')
    search_fields = ('username', 'email')

    # Group fields into sections on the user edit page in admin
    fieldsets = (
            (None, {'fields': ('username', 'password', 'role')}),
            ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
            ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        )

    # Fields shown on the first page when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role'),
        }),
    )

admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(Student)
