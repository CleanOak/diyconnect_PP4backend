# Generated by Django 5.1.1 on 2024-09-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='no_image_mvrwpr', upload_to='images/'),
        ),
    ]
