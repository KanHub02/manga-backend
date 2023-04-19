from django.core.management.base import BaseCommand
from manga.models import Manga, Genre
import requests


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}
domen = "https://remanga.org/media/"


class Command(BaseCommand):
    url = "https://api.remanga.org/api/activity/comments/?title_id=8813&page=2&ordering=&count=20"
    url_comments = "https://api.remanga.org/api/activity/comments/?title_id=8813&page=2&ordering=&count=20"
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
    }
    domen = "https://remanga.org"
    media_domen = "https://remanga.org"

    help = "Parsing manga"

    for i in range(1, 1000):
        url = (
            "https://api.remanga.org/api/titles/recommendations/?&count=20&page="
            + str(i)
        )
        request = requests.get(url=url, headers=HEADERS)
        request_data = request.json()

        for item in request_data["content"]:
            global url2
            url2 = f"https://api.remanga.org/api/titles/" + item["dir"] + "/"
            genre_filter_set = item["genres"]
            manga = Manga.objects.create(
                title_id=item["id"],
                en_name=item["en_name"],
                ru_name=item["rus_name"],
                slug=item["dir"],
                image=media_domen + item["cover_high"],
                type=item["type"],
                issue_year=item["issue_year"],
                rating=item["avg_rating"],
                views=item["total_views"],
                likes=item["total_votes"],
                chapters_quantity=item["count_chapters"],
            )
            for i in genre_filter_set:
                global genre_filter_name
                genre_filter_name = i["name"]
                print("Manga genre -- successfully")
                manga.genre.add(*Genre.objects.filter(title=genre_filter_name))

            detail_request = requests.get(url=url2, headers=HEADERS)
            detail_data = detail_request.json()
            print("Manga -- created")
            try:
                created_manga = Manga.objects.filter(slug=detail_data["content"]["dir"])
            except:
                continue
            for m in created_manga:
                print("Manga description -- updated")
                description = detail_data["content"]["description"]
                manga = Manga.objects.filter(en_name=m)
                manga.update(description=description)
