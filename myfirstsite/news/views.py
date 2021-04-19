from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import News, Category


def index(request):
    context = {'title': 'Главная'}
    return render(request, 'news/index.html', context=context)


def news(request):
    news_list = News.objects.order_by('-created_at')
    context = {
        'title': 'Список новостей',
        'news': news_list,
    }

    return render(request, 'news/news_list.html', context=context)


def get_category_news(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'title': category.title,
        'category_id': category_id,
        'news': news,
    }

    return render(request, 'news/news_list.html', context=context)


def view_news(request, category_id, news_id):
    item = get_object_or_404(News, pk=news_id)

    return render(request, 'news/news_detail.html', context={'news': item})
