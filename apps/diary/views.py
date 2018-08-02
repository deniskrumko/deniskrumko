from datetime import date

from django.http.response import HttpResponseRedirect
from django.utils import timezone
import calendar
from dateutil.rrule import DAILY, rrule
from core.views import BaseView
from django.shortcuts import reverse
from .models import DiaryEntry

__all__ = ('DiaryIndexView', 'DiaryDetailView', 'DiaryEditView')

DATE_FORMAT = '%Y-%m-%d'


class DiaryIndexView(BaseView):
    template_name = 'diary/index.html'
    title = 'DK - Дневник'
    menu = 'diary'

    def get(self, request):

        context = self.get_context_data()

        if not request.user.is_superuser:
            return self.render_to_response(context)

        current = timezone.now()

        last_day_of_month = calendar.monthrange(current.year, current.month)[1]

        existing_entries = {
            entry.date: True if entry.date else False
            for entry in DiaryEntry.objects.filter(
                author=request.user,
            ).exclude(text="")
        }

        days = []
        for dt in rrule(
            DAILY,
            dtstart=date(current.year, current.month, 1),
            until=date(current.year, current.month, last_day_of_month)
        ):
            if dt.day == 1:
                for i in range(dt.weekday()):
                    days.append('-')

            days.append(
                (dt.date(), existing_entries.get(dt.date(), False))
            )

        for i in range(7 - dt.weekday()):
            days.append('-')

        last_days = [
            current - timezone.timedelta(days=i)
            for i in range(0, 6)
        ]

        for index, d in enumerate(last_days):
            last_days[index] = {
                'day': d,
                'entry': DiaryEntry.objects.filter(
                    date=d, author=self.request.user
                ).first()
            }

        context.update({
            'entries': DiaryEntry.objects.all(),
            'days': days,
            'current': current,
            'last_days': last_days,
        })
        return self.render_to_response(context)


class DiaryCalendarView(BaseView):
    template_name = 'diary/calendar.html'
    menu = 'diary'
    title = 'DK - Календарь'

    def get(self, request):
        context = self.get_context_data()
        current = timezone.now()
        context['months'] = [
            timezone.datetime(year=1993, month=i, day=1) for i in range(1, 13)
        ]
        context['years'] = [
            current.year - i
            for i in range(0, 20)
        ]
        return self.render_to_response(context)


class DiaryDetailView(BaseView):
    template_name = 'diary/detail.html'
    menu = 'diary'

    def get_title(self):
        return f'DK - {self.date_obj.strftime("%d.%m.%Y")}'

    def get_entry(self, date, author):
        return DiaryEntry.objects.filter(author=author, date=date).first()

    def get(self, request, date):
        self.date_obj = timezone.datetime.strptime(date, DATE_FORMAT)
        self.entry = self.get_entry(date=date, author=request.user)

        context = self.get_context_data()
        context['entry'] = self.entry
        context['date_str'] = date
        context['date_obj'] = self.date_obj
        return self.render_to_response(context)


class DiaryEditView(DiaryDetailView):
    template_name = 'diary/edit.html'
    menu = 'diary'

    def post(self, request, date):
        text = request.POST.get('text')

        DiaryEntry.objects.update_or_create(
            author=request.user,
            date=date,
            defaults={
                'text': text
            }
        )

        return HttpResponseRedirect(reverse('diary:detail', args=(date,)))
