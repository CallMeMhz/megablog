from django.db import models
from django.contrib import admin
from uuslug import uuslug


class Post(models.Model):
    # slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField(null=True, blank=True)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Post, self).save(*args, **kwargs)


# admin.site.register(Post)
