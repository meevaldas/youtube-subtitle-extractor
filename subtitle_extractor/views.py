import googleapiclient.discovery
import requests
from django.shortcuts import render

from extract_yt_subtitle.settings import DEVELOPER_KEY


def home(request):
    return render(request, 'home.html')


def extractor_main(request):
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

    video_url = request.GET.get('youtube_link')
    video_id = video_url.split("?v=")[1]
    req = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )
    response = req.execute()
    return render(response, 'home_main.html')