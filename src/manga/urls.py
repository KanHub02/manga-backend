from django.urls import path

from .views import MangaListView, MangaRetriveView, MangaCommentsView
from common.views import GlobalSearchView


urlpatterns = [
    path("manga/", MangaListView.as_view(), name="manga-list"),
    path("manga/<slug:slug>/", MangaRetriveView.as_view(), name="manga-detail"),
    path("manga/<slug>/comments/", MangaCommentsView.as_view(), name="manga-comment"),
    path("search/", GlobalSearchView.as_view(), name="global-seach"),
]
