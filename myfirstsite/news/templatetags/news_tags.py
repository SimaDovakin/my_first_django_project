from django import template
from django.db.models import Count, F

from news.models import Category


register = template.Library()


@register.simple_tag()
def get_categories():
    cats = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return cats


@register.inclusion_tag('news/categories_list.html')
def show_categories(category_id=''):
    categories = Category.objects.all()

    return {'categories': categories, 'category_id': category_id}
