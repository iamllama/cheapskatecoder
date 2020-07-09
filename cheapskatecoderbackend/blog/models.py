import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify


def _save_blog_upload_image_files(instance, filename):
    pass

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)
    blog_image = models.FileField(null=True, blank=True, max_length=255)
    meta_summary = models.TextField(null=True, blank=True)
    blog_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_saved_draft = models.DateTimeField(auto_now_add=True)
    series = models.ManyToManyField('series', null=True, blank=True)
    categories = models.ManyToManyField('category', null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.is_published)
    
    def save(self, *args, **kwargs):
        slugged = slugify(self.title)
        self.slug = slugged

        if self.is_published:
            self.date_published = timezone.now()
        super(Blog, self).save(*args, **kwargs)
    

class Series(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

