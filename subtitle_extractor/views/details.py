from django.shortcuts import render


def details(request, id,  *args, **kwargs):
    context = {'embd': f'https://www.youtube.com/embed/{id}'}
    return render(request, 'details.html', context)
