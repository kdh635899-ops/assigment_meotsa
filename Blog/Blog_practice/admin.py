from django.contrib import admin
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)