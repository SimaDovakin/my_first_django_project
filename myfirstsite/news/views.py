from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import News, Category
from .forms import NewsForm


def index(request):
    context = {'title': 'Главная'}
    return render(request, 'news/index.html', context=context)


class NewsList(ListView):
    model = News
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Список новостей"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


# def news(request):
#     news_list = News.objects.order_by('-created_at')
#     context = {
#         'title': 'Список новостей',
#         'news': news_list,
#     }
#
#     return render(request, 'news/news_list.html', context=context)


class NewsByCategory(ListView):
    model = News
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, pk=self.kwargs['category_id'])
        context['title'] = category.title
        context['category_id'] = category.pk
        return context


# def get_category_news(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = get_object_or_404(Category, pk=category_id)
#     context = {
#         'title': category.title,
#         'category_id': category_id,
#         'news': news,
#     }
#
#     return render(request, 'news/news_list.html', context=context)

class ViewNews(DetailView):
    model = News


def view_news(request, category_id, news_id):
    item = get_object_or_404(News, pk=news_id)

    return render(request, 'news/news_detail.html', context={'news': item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
