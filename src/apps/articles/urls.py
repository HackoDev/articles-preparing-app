from django.urls import path

from apps.articles.views import ArticleView

urlpatterns = [
    path('article/<int:pk>/', ArticleView.as_view(), name='articles')
]
