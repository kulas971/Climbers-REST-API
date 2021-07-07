# Generated by Django 3.2.3 on 2021-07-05 18:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members', through='rooms.Membership', to=settings.AUTH_USER_MODEL),
        ),
    ]
