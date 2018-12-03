from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from markdownx.models import MarkdownxField


class Category(models.Model):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    name = models.CharField(_('name'), max_length=128)


class Article(models.Model):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=True, related_name='articles', verbose_name=_('category')
    )
    title = models.CharField(_('title'), max_length=128)
    content = MarkdownxField(_('content'), default='')
    html_content = models.TextField(_('compiled HTML content'), default='', editable=False)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def get_absolute_url(self):
        return reverse('articles', kwargs={'pk': self.pk})


class UsefulLink(models.Model):

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = _('useful url')
        verbose_name_plural = _('useful urls')

    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name=_('category'), related_name='links'
    )
    name = models.TextField(_('name'))
    url = models.CharField(_('url'), max_length=1024)
    description = models.TextField(_('description'))
