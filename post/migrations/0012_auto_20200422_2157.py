# Generated by Django 3.0.4 on 2020-04-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='post.Category'),
        ),
    ]
