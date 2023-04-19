from manga.models import Genre, Manga
from users.models import User, Comment
from common.settings import GENRELIST

import requests
import random


class Scrap:
    url = "https://api.remanga.org/api/activity/comments/?title_id=8813&page=2&ordering=&count=20"
    url_comments = "https://api.remanga.org/api/activity/comments/?title_id=8813&page=2&ordering=&count=20"
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
    }
    domen = "https://remanga.org"
    media_domen = "https://remanga.org"

    @classmethod
    def scrap_users(cls):
        for page in range(10, 100):
            url = f"https://api.remanga.org/api/activity/comments/?title_id=80{str(page)}{str(page)}&page={str(page)}&ordering=&count=20"

            response = requests.get(url=url, headers=cls.HEADERS)
            data = response.json()
            for i in data["content"]:
                User.objects.get_or_create(
                    username=i["user"]["username"],
                    image=cls.media_domen + i["user"]["avatar"]["high"],
                    password="useruser123",
                )
                if User.objects.filter(username=i["user"]["username"]).exists():
                    continue

    @classmethod
    def scrap_comments(cls):
        manga_instance = Manga.objects.all()
        if len(manga_instance) > 0:
            while manga_instance.count() < 4000:
                for i in range(1, 100):
                    instance = Manga.objects.all().values_list("title_id", flat=True)
                    for i in instance:
                        url = f"https://api.remanga.org/api/activity/comments/?title_id={i}&page=2&ordering=&count=20"
                        response = requests.get(url=url, headers=cls.HEADERS)
                        data = response.json()
                        for h in Manga.objects.filter(title_id=i):
                            for i in data["content"]:
                                try:
                                    Comment.objects.create(
                                        user=random.choice(User.objects.all()),
                                        text=i["text"],
                                        manga=h,
                                    )
                                except TypeError:
                                    continue
            return f"Comments count over 3999"
        print("Can't find manga")

    @classmethod
    def scrap_manga(cls):
        for i in range(1, 1000):
            url = (
                "https://api.remanga.org/api/titles/recommendations/?&count=20&page="
                + str(i)
            )
            request = requests.get(url=url, headers=cls.HEADERS)
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
                    image=cls.media_domen + item["cover_high"],
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

                    manga.genre.add(*Genre.objects.filter(title=genre_filter_name))
                detail_request = requests.get(url=url2, headers=cls.HEADERS)
                detail_data = detail_request.json()
                try:
                    created_manga = Manga.objects.filter(
                        slug=detail_data["content"]["dir"]
                    )
                except:
                    continue
                for m in created_manga:
                    description = detail_data["content"]["description"]
                    manga = Manga.objects.filter(en_name=m)
                    manga.update(description=description)


def create_genre(self, *args, **kwargs):
    for i in GENRELIST:
        Genre.objects.get_or_create(title=i)
