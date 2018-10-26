from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DiaryConfig(AppConfig):
    """Configuration for ``Diary`` app."""

    name = 'apps.diary'
    verbose_name = _('Diary')
