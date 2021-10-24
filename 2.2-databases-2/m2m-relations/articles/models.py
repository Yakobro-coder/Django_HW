from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scop = models.ManyToManyField('Tag', through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def main_tag(self):
        return self.scopes.all().get(is_main=True).tag.name
    main_tag.short_description = 'Основной тэг'


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name='Тэг')

    class Meta:
        verbose_name = 'Тэги'
        verbose_name_plural = 'Тэги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Scope(models.Model):
    article = models.ForeignKey(Article, related_name='scopes', verbose_name='Закреплённые Статьи', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='tag', verbose_name='Тэг', on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, verbose_name='Главный тэг')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['-is_main', '-tag']
