# Generated by Django 2.1.5 on 2019-07-30 15:15

import core.models.base_model
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=core.models.base_model.BaseModel.obfuscated_upload, verbose_name='Image'),
        ),
    ]