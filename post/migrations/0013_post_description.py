# Generated by Django 3.0.4 on 2020-04-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20200422_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default=123, max_length=5000),
            preserve_default=False,
        ),
    ]
