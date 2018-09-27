from django.urls import path

from .views import NewsView

app_name = 'apps.news'

urlpatterns = [
    path('', NewsView.as_view(), name='index'),
]
