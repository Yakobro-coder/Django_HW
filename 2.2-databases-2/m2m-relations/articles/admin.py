from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from articles.models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        list_is_main = []
        for form in self.forms:
            list_is_main.append(form.cleaned_data.get('is_main'))
        print(list_is_main.count(True))
        if list_is_main.count(True) > 1:
            raise ValidationError('Основным может быть тольго один тэг')
        elif list_is_main.count(True) < 1:
            raise ValidationError('Укажите основной тэг')
        return super().clean()


class ScopeInLine(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_tag', 'published_at')
    inlines = [ScopeInLine]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine]
    extra = 1
