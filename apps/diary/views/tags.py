from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _

from ..models import DiaryTag
from .diary import BaseDiaryView

__all__ = (
    'DiaryTagsIndexView',
    'DiaryTagsDetailView',
)


class DiaryTagsIndexView(BaseDiaryView):
    """View to get index page for diary tags."""

    template_name = 'diary/tags/index.html'
    title = 'DK - Тэги'
    description = 'Тэги дневника'

    def get_context_data(self):
        """Get context data."""
        context = super().get_context_data()
        context['tags'] = DiaryTag.objects.filter(author=self.user)
        return context


class DiaryTagsDetailView(BaseDiaryView):
    """View to get single tag info."""

    template_name = 'diary/tags/detail.html'

    def get_title(self, **kwargs):
        """Get `title` field value."""
        item = kwargs.get('item')
        return f'DK - #{item.name}' if item else ''

    def get_description(self, **kwargs):
        """Get `description` field value."""
        item = kwargs.get('item')
        return item.name if item else ''

    def get(self, request, tag):
        """Get tag details."""
        item = get_object_or_404(DiaryTag, name=tag, author=self.user)
        years = item.entries.values_list(
            'date__year', flat=True
        ).order_by('-date__year').distinct()
        context = self.get_context_data(item=item)
        context['tag'] = item
        context['stats'] = [(_('Total'), item.entries.count())] + [
            (year, item.entries.filter(date__year=year).count())
            for year in years
        ]
        return self.render_to_response(context)
