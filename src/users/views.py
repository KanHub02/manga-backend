from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from .models import User, Comment
from .services import UserService
from .serializers import (
    SignInSerializer,
    SignUpSerializer,
    AddToFavoriteSerializer,
    ProfileSerializer,
)
from manga.models import Manga
from common.exceptions import UserNotFoundException, MangaNotFoundException


class SignUpView(generics.CreateAPIView):
    queryset = UserService.model.objects.all()
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            UserService.create_user(serializer.validated_data)
            return response.Response(
                data={"message": "Created", "status": 201, "content": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return response.Response(
            {"message": "Bad request", "code": 400, "detail": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class SignInView(generics.GenericAPIView):
    queryset = UserService.model.objects.all()
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.data["username"],
                password=serializer.data["password"],
            )
            return response.Response(
                data={
                    "message": "Ok",
                    "status": 200,
                    "content": UserService.generate_token(user=user),
                },
                status=status.HTTP_200_OK,
            )

        return response.Response(
            {"message": "Bad request", "status": 400, "detail": serializer.errors}
        )
