from common.settings import GENRELIST
from manga.models import Genre
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create genres"

    def handle(self, *args, **kwargs):
        for i in GENRELIST:
            print("Genre -- created")
            Genre.objects.get_or_create(title=i)
