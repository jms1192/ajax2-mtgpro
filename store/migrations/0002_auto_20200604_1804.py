# Generated by Django 3.0.6 on 2020-06-04 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store_event_post',
            name='store',
        ),
        migrations.RemoveField(
            model_name='store_promotion_post',
            name='store',
        ),
    ]