from django.contrib import admin

import sys
from .models import Comment
sys.path.append("..")
from custom_site import custom_site

# Register your models here.

@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')