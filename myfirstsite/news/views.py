from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, logout, login
from django.core.paginator import Paginator
from django.contrib import messages

from .models import News, Category
from .forms import NewsForm, RegisterForm, LoginForm


def index(request):
    news_on_main = News.objects.filter(on_main=True)
    context = {
        'title': 'Главная',
        'news_on_main': news_on_main
    }
    return render(request, 'news/index.html', context=context)


def test(request):
    items = [f'item {i}' for i in range(1, 12)]
    paginator = Paginator(items, 2)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_obj})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались.")
            return redirect('login')
        else:
            messages.error(request, "Что-то пошло не так.")
    else:
        form = RegisterForm()
    return render(request, 'news/register.html', {'form': form})


def my_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Вы успешно авторизованы.")
            return redirect('home')
        else:
            messages.error(request, "Неправильное имя пользователя или пароль.")

    else:
        form = LoginForm()
    return render(request, 'news/login.html', {'form': form})


def my_logout(request):
    logout(request)
    return render(request, 'news/logout.html')


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
