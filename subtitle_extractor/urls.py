from django.urls import path

from subtitle_extractor.views import home, redirect_with_id, details


app_name = "subtitle_extractor"

urlpatterns = [
    path('', home),
    path('video/', redirect_with_id),
    path('video/<str:id>', details)
    # path('id/subtitle/', views.extract_subtitles)
]
