from core.views import BaseView
from django.shortcuts import get_object_or_404

from .models import News


class NewsView(BaseView):
    """View for index page."""
    template_name = 'news/index.html'
    menu = 'news'
    title = 'DK - Новости'
    description = 'Новости сайта'
    use_analytics = True

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'items': News.objects.all(),
        })
        return context


class NewsDetailView(BaseView):
    """View to get detail info about one news."""
    template_name = 'news/detail.html'
    menu = 'news'
    use_analytics = True

    def get_title(self, **kwargs):
        item = kwargs.get('item')
        return f'DK - {item.title}' if item else ''

    def get_description(self, **kwargs):
        item = kwargs.get('item')
        return item.preview if item else ''

    def get(self, request, slug):
        item = get_object_or_404(News, slug=slug)
        context = super().get_context_data(item=item)
        context.update({'item': item})
        return self.render_to_response(context)
