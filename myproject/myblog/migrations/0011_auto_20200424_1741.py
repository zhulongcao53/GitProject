# Generated by Django 3.0.2 on 2020-04-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_auto_20200424_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='Images',
            field=models.ImageField(height_field=254, upload_to='images', verbose_name='图片', width_field=254),
        ),
    ]