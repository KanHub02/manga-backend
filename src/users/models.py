from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, models.Model):
    username = models.CharField(max_length=50, unique=True)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    image = models.URLField(
        null=True, blank=True, verbose_name="Ссылка на картинку из другого источника"
    )
    image_file = models.ImageField(
        upload_to="back_media/uploaded_media",
        null=True,
        blank=True,
        verbose_name="Картинка",
    )
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Комментатор")
    manga = models.ForeignKey(
        "manga.Manga",
        on_delete=models.CASCADE,
        related_name="manga_comments",
        verbose_name="Манга",
    )
    text = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="Текст"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.user} Прокомментровал {self.manga}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
