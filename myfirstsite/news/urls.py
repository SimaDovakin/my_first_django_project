from django.urls import path

from .views import *


urlpatterns = [
    path('', news, name='news_list'),
    path('<int:category_id>/', get_category_news, name='category'),
    path('<int:category_id>/<int:news_id>/', view_news, name='news_detail'),
]
