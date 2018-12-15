from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from markdownx.admin import MarkdownxModelAdmin

from apps.articles.models import Article, Category, UsefulLink


class ArticleAdmin(MarkdownxModelAdmin):
    list_filter = ('category',)


class UsefulLinkAdmin(admin.ModelAdmin):
    list_filter = ('category',)


admin.site.site_header = _('CRM Administration')
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(UsefulLink, UsefulLinkAdmin)
