from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.

class Tags(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(default='', blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_by_tags', kwargs={
            'name':self.title
        })


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(default='', blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_by_category', kwargs={
            'name':self.title
        })
#    class Meta:
#        app_label = 'featured'
#        managed = True

class Post(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=5000)
    content = RichTextUploadingField()
    author = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tags)
    slug = models.SlugField(default='', blank=True)
    featured = models.BooleanField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })

    def get_year(self):
        return self.timestamp.strftime("%Y")

    def get_month(self):
        return self.timestamp.strftime("%B")

    def get_day(self):
        return self.timestamp.strftime("%d")



    #class Meta:
    #    app_label = 'post'
    #    managed = True
