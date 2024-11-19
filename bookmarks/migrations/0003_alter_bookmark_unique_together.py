# Generated by Django 4.2 on 2024-11-19 11:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0009_alter_post_image'),
        ('bookmarks', '0002_rename_user_bookmark_owner'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together={('owner', 'post')},
        ),
    ]
