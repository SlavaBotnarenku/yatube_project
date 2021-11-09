from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group(request):
    return HttpResponse('Список групп')


def group_posts(request, text):
    return HttpResponse(f'Список групп {text}')
