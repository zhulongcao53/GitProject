# Generated by Django 3.0.2 on 2020-04-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20200423_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='menulist',
            name='MenuUrl',
            field=models.CharField(default='something', max_length=200),
        ),
    ]