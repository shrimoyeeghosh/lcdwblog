# Generated by Django 3.0.4 on 2020-04-25 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_post_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, default='')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='post.Tags'),
        ),
    ]