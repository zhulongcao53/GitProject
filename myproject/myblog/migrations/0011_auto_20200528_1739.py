# Generated by Django 3.0.2 on 2020-05-28 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_auto_20200528_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.BlogType', verbose_name='标签'),
        ),
    ]
