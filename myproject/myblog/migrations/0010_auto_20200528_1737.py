# Generated by Django 3.0.2 on 2020-05-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_auto_20200528_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Category',
            field=models.CharField(blank=True, max_length=50, verbose_name='标签'),
        ),
    ]