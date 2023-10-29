from django.shortcuts import render


def details(request, *args, **kwargs):
    video_url = request.GET.get('youtube_link')
    vid = video_url.split("?v=")[1]

    embed_link = video_url.replace("watch?v=", "embed/")
    context = {'embd': embed_link}
    return render(request, 'details.html', context)
