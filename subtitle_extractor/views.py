import io
import os
from pathlib import Path
import google.oauth2.credentials
import google_auth_oauthlib.flow
import google_auth_oauthlib
import googleapiclient.discovery
import json
from django.http import JsonResponse
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload
from django.shortcuts import render
from extract_yt_subtitle.settings import DEVELOPER_KEY


def home(request):
    return render(request, 'home.html')


def extractor_main(request):
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"

    SERVICE_ACCOUNT_FILE = Path(__file__).parent / "./service_account.json"

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)

    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    video_url = request.GET.get('youtube_link')
    video_id = video_url.split("?v=")[1]
    req = youtube.captions().list(
        part="snippet",
        videoId=video_id,
    )

    response = req.execute()

    items_list = response['items']
    for item in items_list:
        id = item["id"]
        language = item['snippet']["language"]
    languages = list(dict.fromkeys(language))

    embed_link = video_url.replace("watch?v=", "embed/")

    context = {'lang': languages, 'embd': embed_link}
    return render(request, 'home_main.html', context)



    # return JsonResponse(response)
    # response = JsonResponse(req.execute())

    # select the languages from the json response
    # languages = []
    # language = response.items()
    # for i in language:
    #     languages.append(i.response[i])
    # languages = list(dict.fromkeys(languages))
    # context = {'lang': languages}
    # return render(request, 'home_main.html', context)





# def extractor_main_backup(request):
#     scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
#
#     os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
#     api_service_name = "youtube"
#     api_version = "v3"
#     # client_secrets_file = "./client_secret_file.json"
#     client_secrets_file = Path(__file__).parent / "./client_secret_file.json"
#     flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
#         client_secrets_file,
#         scopes=scopes)
#
#     # flow.redirect_uri = 'https://www.example.com/oauth2callback'
#     # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
#     #     client_secrets_file, scopes)
#     credentials = flow.run_local_server()
#
#     youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials)
#
#     video_url = request.GET.get('youtube_link')
#     video_id = video_url.split("?v=")[1]
#     req = youtube.captions().download(
#         id=video_id,
#         tfmt="srt",
#         tlang="en",
#     )
#     response = req.execute()
#     fh = io.FileIO("sample", "w")
#
#     download = MediaIoBaseDownload(fh, response)
#     complete = False
#     while not complete:
#         status, complete = download.next_chunk()
#     # # print(response)
#     # return HttpResponse(response, content_type='application/octet-stream')
