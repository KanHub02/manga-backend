from rest_framework import generics, response
from rest_framework.permissions import IsAuthenticated

import django_filters

from .services import MangaService
from .serializers import (
    MangaSerializer,
    CommentSerializer,
    CommentAddSerializer,
    MangaDetailSerializer,
)
from .filters import MangaFilterSet
from common.schemas import manga_schema


class MangaListView(generics.ListAPIView):
    queryset = MangaService._model.objects.all()
    serializer_class = MangaSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
    ]
    filterset_class = MangaFilterSet
    schema = manga_schema.MangaListShema()


class MangaRetriveView(generics.RetrieveAPIView):
    queryset = MangaService._model.objects.all()
    serializer_class = MangaDetailSerializer
    lookup_field = "slug"
    schema = manga_schema.MangaDetailShema()

    def get(self, request, slug):
        instance = MangaService.retrive(slug=slug)
        if instance:
            serializer = self.serializer_class(instance, many=False)
            return response.Response(
                data={"message": "Ok", "status": 200, "content": serializer.data}
            )

        return response.Response(
            {
                "message": "Not found",
                "status": 404,
                "content": {},
                "detail": "Object not found",
            }
        )


class MangaCommentsView(generics.RetrieveAPIView):
    queryset = MangaService._model.objects.all()
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = CommentSerializer
    lookup_field = "slug"
    schema = manga_schema.MangaCommentSchema()

    def get(self, request, slug):
        instance = self.get_queryset().filter(slug=slug).first()
        if instance:
            serializer = self.serializer_class(
                instance.manga_comments, many=True, context={"request": request}
            )
            return response.Response(
                {"message": "Ok", "status": 200, "content": serializer.data}
            )

        return response.Response(
            {
                "message": "Not found",
                "status": 404,
                "content": {},
                "detail": "Object not found",
            }
        )

    def post(self, request, slug):
        instance = self.get_queryset().filter(slug=slug).first()
        if instance:
            serializer = CommentAddSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    manga=instance,
                    user=request.user,
                    text=serializer.validated_data.get("text"),
                )
                return response.Response(
                    data={"message": "Ok", "status": 201, "content": serializer.data}
                )

            return response.Response(
                data={
                    "message": "Bad request",
                    "status": 200,
                    "detail": serializer.errors,
                }
            )

        return response.Response(
            {
                "message": "Not found",
                "status": 404,
                "content": {},
                "detail": "Object not found",
            }
        )
