# Generated by Django 4.2 on 2024-11-19 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_image'),
        ('bookmarks', '0004_alter_bookmark_owner_alter_bookmark_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to='posts.post'),
        ),
    ]