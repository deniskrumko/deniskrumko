from core.views import BaseView

from .models import BlogEntry


class BlogIndexView(BaseView):
    template_name = 'blog/index.html'
    menu = 'blog'
    title = 'DK - Блог'
    description = (
        'Блог Дениса Крумко: видео о путешествиях за границу и '
        'на различные музыкальные концерты. Много музыки и много видео :)'
    )

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'items': BlogEntry.objects.filter(is_active=True),
        })
        return context


class BlogDetailView(BaseView):
    template_name = 'blog/detail.html'
    menu = 'blog'

    def get_title(self, **kwargs):
        title = kwargs.get('title')
        return f'DK - {title}'

    def get_description(self, **kwargs):
        return kwargs.get('description')

    def get(self, request, slug):
        item = BlogEntry.objects.filter(slug=slug).first()
        context = self.get_context_data(
            title=item.title,
            description=item.description
        )
        context.update({
            'item': item,
            'degrees': list(range(-15, 15)),
        })
        return self.render_to_response(context)


class BlogDownloadView(BaseView):
    template_name = 'blog/download.html'
    menu = 'blog'

    def get_title(self, **kwargs):
        title = kwargs.get('title')
        return f'DK - {title} - Скачать'

    def get_description(self, **kwargs):
        return kwargs.get('description')

    def get(self, request, slug):
        item = BlogEntry.objects.filter(slug=slug).first()
        context = self.get_context_data(
            title=item.title,
            description=item.description
        )
        context.update({'item': item})
        return self.render_to_response(context)
