from django.shortcuts import render
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
    category = Category.objects.get(pk=category_id)
    context = {
        'title': category.title,
        'category_id': category_id,
        'news': news,
    }

    return render(request, 'news/news_list.html', context=context)
