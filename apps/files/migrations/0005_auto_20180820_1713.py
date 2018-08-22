# Generated by Django 2.0.5 on 2018-08-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20180820_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videofile',
            name='link',
            field=models.TextField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='link_hd',
            field=models.TextField(blank=True, null=True, verbose_name='Link (HD)'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='youtube_link',
            field=models.TextField(blank=True, null=True, verbose_name='Youtube link'),
        ),
    ]