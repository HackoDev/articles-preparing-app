from django.db import models
from django.utils.translation import ugettext_lazy as _
from markdownx.models import MarkdownxField


class Article(models.Model):

    title = models.CharField(_('title'), max_length=128)
    content = MarkdownxField(_('content'), default='')
    html_content = models.TextField(_('compiled HTML content'), default='', editable=False)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')