# Generated by Django 3.0.6 on 2020-06-04 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200604_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='store_event_post',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.store_user'),
        ),
        migrations.AddField(
            model_name='store_promotion_post',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.store_user'),
        ),
    ]