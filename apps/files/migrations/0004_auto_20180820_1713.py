# Generated by Django 2.0.5 on 2018-08-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_auto_20180820_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videofile',
            name='link',
            field=models.URLField(blank=True, max_length=2048, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='link_hd',
            field=models.URLField(blank=True, max_length=2048, null=True, verbose_name='Link (HD)'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='youtube_link',
            field=models.URLField(blank=True, max_length=2048, null=True, verbose_name='Youtube link'),
        ),
    ]
