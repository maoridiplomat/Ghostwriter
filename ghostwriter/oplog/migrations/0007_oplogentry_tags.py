# Generated by Django 3.2.11 on 2022-11-28 18:01

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('oplog', '0006_oplog_mute_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='oplogentry',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
