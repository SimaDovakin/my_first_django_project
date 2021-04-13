from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    context = {'title': 'Главная'}
    return render(request, 'news/index.html', context=context)


def news(request):
    news_list = News.objects.order_by('-created_at')
    context = {'title': 'News List', 'news': news_list}

    return render(request, 'news/news_list.html', context=context)
