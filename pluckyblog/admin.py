from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_posted')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    inlines = [
        CommentInline,
    ]

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)