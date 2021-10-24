from django.contrib import admin

from articles.models import Article, Scope, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

#
# class ArticleScope(admin.TabularInline):
#     model = ArticleScope
#
#
# @admin.register(ArticleScope)
# class ObjectAdmin(admin.ModelAdmin):
#     inlines = [ArticleScope]
