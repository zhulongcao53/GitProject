# Generated by Django 3.0.2 on 2020-05-28 09:28

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_blog_avatar_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.PhotoType', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(upload_to='images', verbose_name='图片'),
        ),
    ]