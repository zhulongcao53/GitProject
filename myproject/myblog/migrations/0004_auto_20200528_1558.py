# Generated by Django 3.0.2 on 2020-05-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_remove_photo_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='url_height',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='url_width',
        ),
        migrations.AlterField(
            model_name='blog',
            name='Images',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='图片'),
        ),
    ]
