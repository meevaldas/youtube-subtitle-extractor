from django.urls import path

from subtitle_extractor.views import home, redirect_with_id


app_name = "subtitle_extractor"

urlpatterns = [
    path('', home, name="home"),
    path('video/', redirect_with_id),
    # path('id/subtitle/', views.extract_subtitles)
]
