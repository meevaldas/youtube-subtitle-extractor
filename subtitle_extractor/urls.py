from django.urls import path
from django.views.generic import RedirectView

from subtitle_extractor.views import home, redirect_with_id, details, subtitles, download_subtitles


app_name = "subtitle_extractor"

urlpatterns = [
    path('', home),
    path('video/', redirect_with_id),
    path('video/<str:id>', details),
    path('video/<str:id>/subtitles/', subtitles),
    path('video/<str:id>/subtitles/<str:cap_id>/', download_subtitles)
]

# https://www.youtube.com/watch?v=9sfvpupkb6k