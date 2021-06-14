from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    save_on_top = True

    list_display = ('id', 'title', 'category',
                    'created_at', 'updated_at',
                    'is_published', 'views', 'get_photo', 'on_main')
    list_display_links = ('id', 'title')
    list_editable = ('is_published', 'category', 'on_main')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'category', 'on_main')
    fields = ('title', 'category', 'content',
              'photo', 'get_photo', 'is_published',
              'created_at', 'updated_at', 'views',
              'on_main')
    readonly_fields = ('get_photo', 'created_at', 'updated_at', 'views')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="60">')
        return "Фото отсутствует"

    get_photo.short_description = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админка "Обучающий проект"'
admin.site.site_header = 'Админка "Обучающий проект"'
