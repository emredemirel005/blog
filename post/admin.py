from django.contrib import admin

# Register your models here.
from .models import Post
from markdownx.admin import MarkdownxModelAdmin

class PostAdmin(MarkdownxModelAdmin):
    list_display = ("slug","title","created_at")
    readonly_fields = ("slug",)

admin.site.register(Post, PostAdmin)