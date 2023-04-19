from rest_framework import serializers, response
from manga.models import Manga
from rest_framework.views import APIView
from django.db.models import Q

from common.schemas import base_schema


class GlobalSearchSerializer(serializers.Serializer):
    promt = serializers.CharField(max_length=255)


class GlobalSearchView(APIView):
    serializer_class = GlobalSearchSerializer
    schema = base_schema.GlobalSearchSchema()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            promt = serializer.data.get("promt")
            if len(promt) >= 3:
                if promt is None:
                    promt = ""
                data = Manga.objects.filter(
                    Q(en_name__icontains=promt) | Q(ru_name__icontains=promt)
                )
                return response.Response(
                    {"status": 200, "content": data.values(), "message": "Ok"}
                )

            return response.Response(
                {
                    "message": "Request must be more than 3 characters",
                    "status": 400,
                    "content": [],
                }
            )

        return response.Response(data=serializer.errors, status=400)
