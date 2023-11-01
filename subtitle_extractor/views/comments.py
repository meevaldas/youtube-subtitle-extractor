import io
import os
import googleapiclient.discovery
from django.shortcuts import render
from googleapiclient.http import MediaIoBaseDownload

from extract_yt_subtitle.settings import DEVELOPER_KEY


def download_comments(request, id, **kwargs):
    comment_list =[]
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    req = youtube.commentThreads().list(
        part="snippet",
        videoId=id,
        maxResults=100
    )
    response = req.execute()
    for item in response['items']:
        comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comment_text = comment_text + '\n'
    comment_list.append(comment_text)
    file_name = f'comments_{id}.txt'
    with open(file_name, "w", encoding="utf-8") as file:
        for item in response['items']:
            comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
            file.write(comment_text + '\n')

    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())




    # fh = io.FileIO("comments_.txt", "wb")
    #
    # download = MediaIoBaseDownload(fh, response['items'])
    # complete = False
    # while not complete:
    #     status, complete = download.next_chunk()

    # with open("comments.txt", "w", encoding="utf-8") as file:
    #     for item in response['items']:
    #         comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
    #         file.write(comment_text + '\n')
    #
    # with open("comments.txt", "r", encoding="utf-8") as file:
    #     for line in file:
    #         print(line.strip())
    # response['parent_id'] = com_id
    # return render(request, 'details.html', response)
