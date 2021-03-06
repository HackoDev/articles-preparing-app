from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('', include('apps.articles.urls')),
    path('jet/', include(('jet.urls', 'jet'))),
]
