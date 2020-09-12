# Generated by Django 2.0.5 on 2018-08-23 14:11

from django.db import migrations, models

import django_extensions.db.fields

import core.models.base_model


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('data', models.FileField(blank=True, null=True, upload_to=core.models.base_model.BaseModel.default_upload, verbose_name='Data')),
                ('link_hd', models.TextField(blank=True, null=True, verbose_name='Link (HD)')),
                ('link', models.TextField(blank=True, null=True, verbose_name='Link')),
                ('youtube_link', models.TextField(blank=True, null=True, verbose_name='Youtube link')),
                ('source', models.CharField(choices=[('file', 'File'), ('youtube', 'Youtube'), ('google_photo', 'Google Photo'), ('source_url', 'Source URL')], default='file', max_length=64, null=True, verbose_name='Source')),
                ('poster', models.ImageField(blank=True, null=True, upload_to=core.models.base_model.BaseModel.obfuscated_upload, verbose_name='Poster image')),
            ],
            options={
                'verbose_name': 'Video file',
                'verbose_name_plural': 'Video files',
            },
        ),
    ]
