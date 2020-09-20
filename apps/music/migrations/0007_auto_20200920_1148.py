# Generated by Django 3.1 on 2020-09-20 08:48

import django.db.models.deletion
from django.db import migrations, models

import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0008_videofile_duration'),
        ('music', '0006_auto_20200911_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='year',
        ),
        migrations.CreateModel(
            name='MusicVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('slug', models.CharField(db_index=True, max_length=64, null=True, unique=True, verbose_name='Slug')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='music_videos', to='music.album', verbose_name='Album')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='music_videos', to='files.videofile', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Music video',
                'verbose_name_plural': 'Music videos',
                'ordering': ('-created',),
            },
        ),
    ]
