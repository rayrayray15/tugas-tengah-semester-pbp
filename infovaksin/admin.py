from django.contrib import admin
from .models import Comment
from . import models

# Register your models here.
admin.site.register(Comment)

# @admin.register(models.Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ("name", "publish")
#     search_fields = ("name", "content")