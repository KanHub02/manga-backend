from django.core.management.base import BaseCommand
from users.models import User, Comment
from manga.models import Manga

import random
import requests


url = "https://api.remanga.org/api/activity/comments/?title_id=8813&page=2&ordering=&count=20"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}


class Command(BaseCommand):
    help = "Parsing data from manga sites, create users and comments"

    def handle(self, *args, **kwargs):
        response = requests.get(url=url, headers=HEADERS)
        data = response.json()
        print("Comment -- created")
        for h in Manga.objects.all():
            for i in data["content"]:
                Comment.objects.create(
                    user=random.choice(User.objects.all()),
                    text=i["text"],
                    manga=h,
                )