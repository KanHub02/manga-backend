from rest_framework import serializers
from .models import Manga, Genre
from users.models import User, Comment
from users.models import Comment


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "title"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "image", "image_file"]


class CommentSerializer(serializers.ModelSerializer):
    user = AuthorSerializer()
    text = serializers.CharField(max_length=255)

    class Meta:
        model = Comment
        fields = ["id", "user", "text"]
        extra_kwargs = {"author": {"read_only": True}}

    def get_count_of_likes(self, obj):
        return Comment.objects.filter(comment=obj).count()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "title"]


class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = "__all__"


class MangaDetailSerializer(serializers.ModelSerializer):
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    comments_count = serializers.SerializerMethodField(method_name="get_comments_count")

    class Meta:
        model = Manga
        fields = [
            "id",
            "en_name",
            "ru_name",
            "type",
            "image",
            "description",
            "genre",
            "chapters_quantity",
            "issue_year",
            "rating",
            "likes",
            "created_at",
            "comments_count",
        ]

    def get_comments_count(self, instance):
        return Comment.objects.filter(manga=instance).count()


class TopMangaSerializer(serializers.ModelField):
    class Meta:
        model = Manga
        fields = [
            "en_name",
            "ru_name",
            "image",
            "genre",
            "rating",
            "type",
        ]


class CommentAddSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()
    text = serializers.CharField(max_length=250)
    manga = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["text", "manga"]


class LikeCommentSerializer(serializers.Serializer):
    user = serializers.CurrentUserDefault()
    comment = serializers.PrimaryKeyRelatedField(read_only=True)
