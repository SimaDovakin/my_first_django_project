from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs = {'news_id': self.pk, 'category_id': self.category.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ["-created_at"]


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Наименование", db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs = {'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ["title"]
