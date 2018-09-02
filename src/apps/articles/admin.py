from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from apps.articles.models import Article


class ArticleAdmin(MarkdownxModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
