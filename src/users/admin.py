from django.contrib import admin
from .models import User, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = (
        "username",
        "image",
        "image_file",
        "favorite_manga",
        "is_superuser",
        "is_staff",
        "is_active",
    )

    readonly_fields = ("id", "created_at", "updated_at")
    list_display = ["username", "image_file"]
    list_display_links = ["username", "image_file"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = (
        "user",
        "manga",
        "text",
    )
    readonly_fields = ("id", "created_at", "updated_at")
    list_display = ["id", "user"]
    list_display_links = ["id", "user"]
