from django.shortcuts import render


def details(request, id):
    context = {'embd': f'https://www.youtube.com/embed/{id}', 'video_id': id}
    return render(request, 'details.html', context)
