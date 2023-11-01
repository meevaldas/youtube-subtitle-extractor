import os
import googleapiclient.discovery
from babel import Locale, UnknownLocaleError
from django.shortcuts import render, redirect
from pathlib import Path
from google.oauth2 import service_account

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
api_service_name = "youtube"
api_version = "v3"

SERVICE_ACCOUNT_FILE = Path(__file__).parent / "../service_account.json"

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)


def subtitles(request, id):
    captions = youtube.captions().list(
        part="snippet",
        videoId=id,
    )

    response = captions.execute()

    items_list = response['items']
    for item in items_list:
        language = item['snippet']["language"]

        # conversion of code to language name
        try:
            locale = Locale(language)
            language_name = locale.english_name

        except UnknownLocaleError:
            language_name = language

        item['natural_language'] = language_name

    return render(request, 'subtitles.html', response)


def download_subtitles(request, id, cap_id):

    caption_str = youtube.captions().download(
        id=cap_id,
        tfmt='srt'
    ).execute()

    caption_data = caption_str.split('\n\n')
    for line in caption_data:
        if line.count('\n') > 1:
            i, cap_time, caption = line.split('\n', 2)
            print('%02d) [%s] %s' % (
                int(i), cap_time, ' '.join(caption.split())))
