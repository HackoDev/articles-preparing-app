from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from apps.articles.models import Article, Category, UsefulLink


class ArticleAdmin(MarkdownxModelAdmin):
    list_filter = ('category',)


class UsefulLinkAdmin(admin.ModelAdmin):
    list_filter = ('category',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(UsefulLink, UsefulLinkAdmin)
