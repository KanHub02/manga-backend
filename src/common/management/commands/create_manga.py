from django.core.management.base import BaseCommand
from manga.models import Manga, Genre
import requests


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}
domen = "https://remanga.org/media/"


class Command(BaseCommand):
    help = "Parsing manga"

    def handle(self, *args: any, **options: any) -> object:
        for i in range(1, 100):
            url = (
                "https://api.remanga.org/api/titles/recommendations/?&count=20&page="
                + str(i)
            )
            request = requests.get(url=url, headers=HEADERS)
            request_data = request.json()

            for item in request_data["content"]:
                global url2
                print("User -- created")
                url2 = f"https://api.remanga.org/api/titles/" + item["dir"] + "/"
                genre_filter_set = item["genres"]
                manga = Manga.objects.create(
                    en_name=item["en_name"],
                    ru_name=item["rus_name"],
                    slug=item["dir"],
                    image=domen + item["cover_high"],
                    type=item["type"],
                    views=item["views"],
                    issue_year=item["issue_year"],
                    rating=item["avg_rating"],
                    likes=item["total_votes"],
                    chapters_quantity=item["count_chapters"],
                )
                for i in genre_filter_set:
                    global genre_filter_name
                    genre_filter_name = i["name"]
                    manga.genre.add(*Genre.objects.filter(title=genre_filter_name))
                detail_request = requests.get(url=url2, headers=HEADERS)
                detail_data = detail_request.json()
                try:
                    created_manga = Manga.objects.filter(
                        dir=detail_data["content"]["dir"]
                    )
                except:
                    continue
                for m in created_manga:
                    description = detail_data["content"]["description"]
                    manga = Manga.objects.filter(en_name=m)
                    manga.update(description=description)
