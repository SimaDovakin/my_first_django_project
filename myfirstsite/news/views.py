from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    return HttpResponse('<h1>Hello, world!</h1>')

def news(request):
    news = News.objects.all()
    title = 'News List'

    return render(request, 'news/news_list.html', context={'news': news, 'title': title})
