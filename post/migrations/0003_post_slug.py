# Generated by Django 3.0.4 on 2020-04-11 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
