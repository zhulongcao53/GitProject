# Generated by Django 3.0.2 on 2020-05-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_auto_20200528_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=50, verbose_name='标签')),
                ('Timestamp', models.DateTimeField(verbose_name='时间')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
                'ordering': ('-Timestamp',),
            },
        ),
    ]