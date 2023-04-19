from .models import Manga, Genre


class MangaService:
    _model = Manga

    @classmethod
    def retrive(cls, slug):
        instance = cls._model.objects.filter(slug=slug)
        if instance is not None:
            return instance.first()
