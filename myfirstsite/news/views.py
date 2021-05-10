from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import News, Category
from .forms import NewsForm, UserRegisterForm


def index(request):
    context = {'title': 'Главная'}
    return render(request, 'news/index.html', context=context)


def test(request):
    items = [f'item {i}' for i in range(1, 12)]
    paginator = Paginator(items, 2)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_obj})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрированы!")
            return redirect('login')
        else:
            messages.error(request, "Ошибка регистрации!")
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def login(request):
    return render(request, 'news/login.html')


class NewsList(ListView):
    model = News
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Список новостей"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_queryset(self):
        return News.objects.filter(
            is_published=True,
            category_id=self.kwargs['category_id']
        ).select_related('category')

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


class CreateNews(LoginRequiredMixin, CreateView):
    login_url = '/admin/'

    form_class = NewsForm
    template_name = 'news/add_news.html'
