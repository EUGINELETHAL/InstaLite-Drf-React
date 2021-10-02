# Generated by Django 2.2.2 on 2019-07-04 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='frontend/public/posts/%Y/%m/%d', verbose_name='post_picture'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='frontend/public/users/%Y/%m/%d', verbose_name='profile_picture'),
        ),
    ]