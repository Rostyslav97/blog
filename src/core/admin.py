from django.contrib import admin
from core import models


class TabularInlineComment(admin.TabularInline):
    model = models.Comment


class TabularInlineUpvote(admin.TabularInline):
    model = models.Upvote


class PostAdmin(admin.ModelAdmin):
    inlines = [TabularInlineComment, TabularInlineUpvote]
    list_display = ("title", "author_name")


admin.site.register(models.Post, PostAdmin)
