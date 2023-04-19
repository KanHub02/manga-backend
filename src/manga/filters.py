from django_filters import rest_framework as filters

from .models import Manga


class MangaFilterSet(filters.FilterSet):
    min_issue_year = filters.NumberFilter(field_name="issue_year", lookup_expr="gte")
    max_issue_year = filters.NumberFilter(field_name="issue_year", lookup_expr="lte")

    class Meta:
        model = Manga
        fields = [
            "genre__title",
            "type",
        ]
