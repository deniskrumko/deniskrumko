from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from core.views import BaseView
from django.db.models import Q
from apps.news.models import News
from apps.music.models import Track
from apps.blog.models import BlogEntry
from apps.diary.models import DiaryEntry
from .models import RedirectPage

__all__ = ('IndexView', 'RedirectView', 'SearchView', 'WakeMyDyno')


class IndexView(BaseView):
    """View for index page."""
    template_name = 'index.html'
    menu = 'index'
    title = 'Denis Krumko'
    description = (
        'Сайт Дениса Крумко: видеоблоги о путешествиях, инструментальная '
        'музыка, ну и все. Смотрите, слушайте, узнавайте.'
    )
    use_analytics = True

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'news_items': News.objects.all()[:4],
            'total_news_count': News.objects.count()
        })
        return context


class RedirectView(View):
    """View to redirect pages."""

    def get(self, request, page=None):
        page = get_object_or_404(RedirectPage, source=page)
        return HttpResponseRedirect(page.destination)


class SearchView(BaseView):
    """View to search page."""
    template_name = 'search.html'
    title = 'DK - Поиск'
    description = 'Поиск данных на сайте deniskrumko.ru'
    menu = 'index'

    def find_music_tracks(self, search_query):
        return Track.objects.filter(
            Q(name__icontains=search_query) |
            Q(short_description__icontains=search_query) |
            Q(full_description__icontains=search_query)
        ).distinct()

    def find_blog_entries(self, search_query):
        return BlogEntry.objects.filter(
            Q(title__icontains=search_query) |
            Q(subtitle__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(text__icontains=search_query)
        ).distinct()

    def find_diary_entries(self, search_query):
        return DiaryEntry.objects.filter(
            text__icontains=search_query
        ).distinct()

    def get(self, request, search_query=None):
        form_search_query = request.GET.get('search_query')

        if not search_query and form_search_query:
            return HttpResponseRedirect(f'/search/{form_search_query}')

        context = self.get_context_data()

        results = {}

        MAX = 10

        if search_query:
            tracks = self.find_music_tracks(search_query)

            if tracks:
                category = 'Музыка'
                if tracks.count() > MAX:
                    category += f' (Показано {MAX} из {tracks.count()})'

                results[category] = [
                    {
                        'title': track.name,
                        'preview': track.short_description[:100],
                        'url': f'/music/{track.slug}'
                    }
                    for track in tracks[:MAX]
                ]

            blogs = self.find_blog_entries(search_query)

            if blogs:
                category = 'Блоги'
                if blogs.count() > MAX:
                    category += f' (Показано {MAX} из {blogs.count()})'

                results[category] = [
                    {
                        'title': blog.title,
                        'preview': blog.subtitle,
                        'url': f'/blog/{blog.slug}'
                    }
                    for blog in blogs[:MAX]
                ]

            if request.user.is_superuser:
                diaries = self.find_diary_entries(search_query)

                if diaries:
                    category = 'Дневник'
                    if diaries.count() > MAX:
                        category += f' (Показано {MAX} из {diaries.count()})'

                    results[category] = [
                        {
                            'title': diary.date,
                            'preview': diary.text[:200] + '...',
                            'url': f'/diary/{diary.date}'
                        }
                        for diary in diaries[:MAX]
                    ]

        context['search_query'] = search_query
        context['categories'] = results

        return self.render_to_response(context)


class WakeMyDyno(View):
    """Simple empty response."""

    def get(self, request, page=None):
        return HttpResponse()
