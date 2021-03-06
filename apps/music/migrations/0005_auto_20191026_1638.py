# Generated by Django 2.1.5 on 2019-10-26 13:38

import django.db.models.deletion
from django.db import migrations, models

import adminsortable.fields
import django_extensions.db.fields
import imagekit.models.fields

import core.models.base_model


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20181024_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=64, null=True, verbose_name='Name')),
                ('slug', models.CharField(max_length=50, null=False, verbose_name='slug', db_index=True)),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Year')),
                ('status', models.CharField(blank=True, max_length=64, null=True, verbose_name='Status')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=core.models.base_model.BaseModel.obfuscated_upload, verbose_name='Image')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
                'ordering': ('order',),
            },
        ),
        migrations.RemoveField(
            model_name='track',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='track',
            name='color',
        ),
        migrations.RemoveField(
            model_name='track',
            name='full_description',
        ),
        migrations.RemoveField(
            model_name='track',
            name='lead',
        ),
        migrations.RemoveField(
            model_name='track',
            name='likes_counter',
        ),
        migrations.RemoveField(
            model_name='track',
            name='short_description',
        ),
        migrations.AddField(
            model_name='track',
            name='duration',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Duration'),
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.AddField(
            model_name='track',
            name='album',
            field=adminsortable.fields.SortableForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tracks', to='music.Album', verbose_name='Album'),
        ),
    ]
