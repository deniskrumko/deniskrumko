from django.core.management import BaseCommand
from django.utils import timezone

from apps.blog.factories import BlogEntryFactory, BlogSeriesFactory, BlogSeriesItemFactory
from apps.diary.factories import DiaryEntryFactory, DiaryTagFactory
from apps.files.factories import FileCategoryFactory, FileFactory
from apps.music.factories import AlbumFactory, TrackFactory, TrackFileFactory
from apps.users.models import User


class Command(BaseCommand):
    """Command to populate database with test data."""

    def create_track(self, album):
        """Create ``Track``."""
        music_file = FileFactory(category=self.music_category)
        gtp_file = FileFactory(category=self.gtp_category)
        track = TrackFactory(album=album, file=music_file)
        TrackFileFactory(track=track, file=music_file)
        TrackFileFactory(track=track, file=gtp_file)
        self.stdout.write(self.style.SUCCESS(f'  {album.name} - {track.name}'))

    def handle(self, *args, **options):
        """Execute command."""
        # Music
        # ====================================================================

        self.stdout.write(self.style.SUCCESS('\n1. Create albums'))
        albums = AlbumFactory.create_batch(4)

        self.music_category = FileCategoryFactory(name='Музыка')
        self.gtp_category = FileCategoryFactory(name='GTP')

        for album in albums:
            for i in range(5):
                self.create_track(album=album)

        # Blog
        # ====================================================================

        self.stdout.write(self.style.SUCCESS('\n2. Create blog entries'))
        blogs = BlogEntryFactory.create_batch(12, create_images=True)

        self.stdout.write(self.style.SUCCESS('\n3. Create blog series'))
        series = BlogSeriesFactory.create_batch(3)
        for index, series_entry in enumerate(series):
            BlogSeriesItemFactory(
                series=series_entry,
                entry=blogs[index],
            )
            BlogSeriesItemFactory(
                series=series_entry,
                entry=blogs[index + 1],
            )

        # Diary
        # ====================================================================

        self.stdout.write(self.style.SUCCESS('\n4. Create diary entries'))
        root = User.objects.first()
        current_time = timezone.now()
        for i in range(30):
            DiaryEntryFactory(
                author=root,
                date=(current_time - timezone.timedelta(days=i)).date(),
            )

        self.stdout.write(self.style.SUCCESS('\n5. Create diary tags'))
        DiaryTagFactory.create_batch(20, author=root)

        # Final
        # ====================================================================

        self.stdout.write(self.style.SUCCESS('DB successfully populated!'))
