from django.contrib import admin
from django.db import models

from .models import Post

from pagedown.widgets import AdminPagedownWidget


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }