from django.http import Http404
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def redirect_with_id(request):
    youtube_link = request.POST.get('youtube_link')

    if not youtube_link:
        raise Http404("Youtube link not found")

    video_parts = youtube_link.split("?v=")

    if len(video_parts) < 2:
        raise Http404("Youtube Video ID not found")

    video_id = video_parts[1]

    if not video_id:
        raise Http404("Video Id not found")

    return redirect(f'/video/{ video_id }')
