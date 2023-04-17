from django.contrib import admin

from .models import Genre, Manga


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    fields = (
        "en_name",
        "ru_name",
        "slug",
        "image",
        "description",
        "chapters_quantity",
        "issue_year",
        "type",
        "genre",
        "likes",
        "views",
        "rating",
    )
    list_display = [
        "en_name",
        "ru_name",
    ]
    list_display_links = [
        "en_name",
        "ru_name",
    ]
    readonly_fields = ["created_at", "id"]
    ordering = ["-issue_year"]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fields = ("title",)


# Register your models here.
