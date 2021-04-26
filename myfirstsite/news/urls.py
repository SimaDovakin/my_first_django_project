from django.urls import path

from .views import *


urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('<int:category_id>/<int:news_id>/', view_news, name='news_detail'),
    path('add-news/', add_news, name='add_news'),
]
