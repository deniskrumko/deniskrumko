# Generated by Django 2.1.5 on 2020-04-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_auto_20181015_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='videofile',
            name='duration',
            field=models.CharField(blank=True, help_text='For example: 15:00', max_length=8, null=True, verbose_name='Video duration'),
        ),
    ]
