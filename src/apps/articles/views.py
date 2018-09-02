from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from apps.articles.models import Article


class ArticleView(LoginRequiredMixin, DetailView):

    template_name = 'article.html'
    queryset = Article.objects.all()
