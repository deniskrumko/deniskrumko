from django.db import models
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import SortableMixin
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit
from adminsortable.fields import SortableForeignKey
from libs.autoslug import AutoSlugField

from core.models import BaseModel


class Artist(SortableMixin, BaseModel):
    """Model for artist information."""
    name = models.CharField(
        max_length=64,
        null=True,
        blank=False,
        verbose_name=_('Name')
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
        verbose_name=_('Order'),
    )

    def __str__(self):
        return self.name or '-'

    class Meta:
        verbose_name = _('Artist')
        verbose_name_plural = _('Artists')
        ordering = ('order',)


class Track(SortableMixin, BaseModel):
    """Model for storing track's information.

    Attributes:
        is_active (bool): display track on site or not.
        name (str): name of track.
        year (int): year, when track was created.
        slug (str): slug from track name.
        file (File): related ``File`` model.
        image (File): image file.
        description (str): track description.

    """
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is active'),
    )
    artist = SortableForeignKey(
        Artist,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='tracks',
        verbose_name=_('Artist'),
    )
    name = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        verbose_name=_('Name')
    )
    year = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_('Year'),
    )
    slug = AutoSlugField(
        populate_from='name',
        unique_with=('name',),
        verbose_name=_('Slug'),
    )
    file = models.ForeignKey(
        'files.File',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='tracks',
        verbose_name=_('File'),
    )
    image = ProcessedImageField(
        null=True,
        blank=True,
        processors=[ResizeToFit(800, 800)],
        format='JPEG',
        options={'quality': 100},
        upload_to=BaseModel.obfuscated_upload,
        verbose_name=_('Image'),
    )
    image_thumbnail = ProcessedImageField(
        null=True,
        blank=True,
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 90},
        upload_to=BaseModel.obfuscated_upload
    )
    short_description = models.TextField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Short description'),
        help_text=_('Displayed on "All tracks" page')
    )
    full_description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Full description'),
        help_text=_('Displayed on "Single track" page')
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
        verbose_name=_('Order'),
    )

    def __str__(self):
        return f'{self.artist} - {self.name}'

    class Meta:
        verbose_name = _('Track')
        verbose_name_plural = _('Tracks')
        ordering = ('-order',)

    def save(self, *args, **kwargs):
        if not self.id:
            self.order = 0

        super().save(*args, **kwargs)


class TrackFile(SortableMixin, models.Model):
    """Intermediate model for M2M related between ``Track`` and ``File``."""
    track = models.ForeignKey(
        Track,
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='related_files',
        verbose_name=_('Track'),
    )
    file = models.ForeignKey(
        'files.File',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='related_tracks',
        verbose_name=_('File'),
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
        verbose_name=_('Order'),
    )

    def __str__(self):
        return self.file.name if self.file else '-'

    class Meta:
        verbose_name = _('Track file')
        verbose_name_plural = _('Track files')
        ordering = ('order',)
