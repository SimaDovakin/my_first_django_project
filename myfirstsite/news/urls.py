from django.urls import path

from .views import *


urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('<int:category_id>/<int:news_id>/', ViewNews.as_view(), name='news_detail'),
    path('add-news/', CreateNews.as_view(), name='add_news'),
]
