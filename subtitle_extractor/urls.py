from django.urls import path
from . import views

app_name = "subtitle_extractor"

urlpatterns = [
    path('', views.home),
    path('download/', views.extractor_main)
]
