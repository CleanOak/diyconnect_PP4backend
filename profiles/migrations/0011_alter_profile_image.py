# Generated by Django 5.1 on 2024-09-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../nobody_nruqan', upload_to='images/'),
        ),
    ]