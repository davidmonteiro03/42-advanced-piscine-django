from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Personalized permissions', {'fields': ('can_downvote_tips',)}),
        ('Reputation points', {'fields': ('rep_points',)}),
    )
