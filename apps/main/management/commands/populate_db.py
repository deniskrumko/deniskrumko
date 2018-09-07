from django.core.management import BaseCommand

from apps.blog.factories import BlogEntryFactory
from apps.files.factories import FileCategoryFactory, FileFactory
from apps.music.factories import ArtistFactory, TrackFactory, TrackFileFactory
from apps.news.factories import NewsFactory


class Command(BaseCommand):
    """Command to populate database with test data."""

    def create_track(self, artist):
        music_file = FileFactory(category=self.music_category)
        gtp_file = FileFactory(category=self.gtp_category)
        track = TrackFactory(artist=artist, file=music_file)
        TrackFileFactory(track=track, file=music_file)
        TrackFileFactory(track=track, file=gtp_file)
        self.stdout.write(self.style.SUCCESS(f'{artist.name} - {track.name}'))

    def handle(self, *args, **options):
        # Music
        # ====================================================================

        dendynotdead = ArtistFactory(name='Dendy Not Dead')

        self.music_category = FileCategoryFactory(name='Музыка')
        self.gtp_category = FileCategoryFactory(name='GTP')

        for i in range(10):
            self.create_track(artist=dendynotdead)

        # Blog
        # ====================================================================

        BlogEntryFactory.create_batch(2, create_items=True, create_images=True)
        self.stdout.write(self.style.SUCCESS('\nCreated blog entries'))

        # News
        # ====================================================================

        NewsFactory.create_batch(10)
        self.stdout.write(self.style.SUCCESS('\nCreated news'))

        self.stdout.write(self.style.SUCCESS(
            '\nDatabase successfully populated!'
        ))
