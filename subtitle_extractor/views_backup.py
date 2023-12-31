import os
from pathlib import Path
from babel import Locale
import googleapiclient.discovery
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload
from django.shortcuts import render
from pytube import YouTube
from extract_yt_subtitle.settings import DEVELOPER_KEY





def extract_subtitles(request):
    # scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    # api_service_name = "youtube"
    # api_version = "v3"
    #
    # SERVICE_ACCOUNT_FILE = Path(__file__).parent / "./service_account.json"
    #
    # credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
    #
    # youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    # video_url = request.GET.get('youtube_link')
    # video_url = request.build_absolute_uri()
    # video_id = video_url.split("%3D")[1]

    req = youtube.captions().list(
        part="snippet",
        videoId=video_id,
    )

    response = req.execute()

    items_list = response['items']
    for item in items_list:
        id = item["id"]
        language = item['snippet']["language"]
        if language:
            if language == 'en-US':
                language = 'English - US'
            elif language == 'zh-Hant':
                language = 'Chinese'
            else:
                locale = Locale(language)
                language = locale.english_name
        else:
            language = id
        item['natural_language'] = language

    return render(request, 'subtitles.html', response)


