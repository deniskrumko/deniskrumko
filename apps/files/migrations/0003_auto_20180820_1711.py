# Generated by Django 2.0.5 on 2018-08-20 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_videofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='videofile',
            name='link_hd',
            field=models.URLField(blank=True, max_length=512, null=True, verbose_name='Link (HD)'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='youtube_link',
            field=models.URLField(blank=True, max_length=512, null=True, verbose_name='Youtube link'),
        ),
    ]
