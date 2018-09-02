from django.apps import AppConfig
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _

from apps.articles.signal_handlers import article_pre_save


class ArticlesConfig(AppConfig):
    name = 'apps.articles'
    verbose_name = _('articles')

    def ready(self):
        # article save handler
        pre_save.connect(article_pre_save, sender=self.models['article'])
