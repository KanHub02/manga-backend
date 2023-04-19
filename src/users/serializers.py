from rest_framework import serializers
from .services import UserService
from .models import User, Comment
from manga.models import Manga


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=5, max_length=35)
    nickname = serializers.CharField(min_length=5, max_length=35, required=False)
    password = serializers.CharField(min_length=8, max_length=50, write_only=True)
    image_file = serializers.ImageField(write_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "nickname",
            "password",
            "image_file",
        )


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=35)
    password = serializers.CharField(min_length=3, max_length=50)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "favorite_manga"]


class AddToFavoriteSerializer(serializers.ModelSerializer):
    favorite_manga = serializers.SlugRelatedField(slug_field=Manga.slug, read_only=True)

    class Meta:
        model = Manga
        fields = ("favorite_manga",)
