from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

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


class ViewNews(DetailView):
    model = News
    pk_url_kwarg = 'news_id'

    def get_object(self):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
