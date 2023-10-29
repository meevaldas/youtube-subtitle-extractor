from django.urls import path
from . import views

app_name = "subtitle_extractor"

urlpatterns = [
    path('', views.home),
    path('id/', views.extract_video),
    path('id/subtitle/', views.extract_subtitles)
]
