# Generated by Django 3.0.2 on 2020-04-24 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=50, verbose_name='标签')),
                ('Timestamp', models.DateTimeField(verbose_name='时间')),
            ],
            options={
                'verbose_name': '图片标签',
                'verbose_name_plural': '图片标签',
                'ordering': ('-Timestamp',),
            },
        ),
    ]