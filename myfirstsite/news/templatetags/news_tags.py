from django import template

from news.models import Category


register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/categories_list.html')
def show_categories(category_id=''):
    categories = Category.objects.all()

    return {'categories': categories, 'category_id': category_id}
