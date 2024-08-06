from django.contrib import admin

from .models import Forum, Post, Comment, Like
# Register your models here.

class ForumAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'forum', 'content', 'created_at')
    search_fields = ('user__username', 'content')
    list_filter = ('forum', 'created_at')
    ordering = ('-created_at',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_at')
    search_fields = ('user__username', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')
    search_fields = ('user__username', 'post__content')
    list_filter = ('post', 'user')

admin.site.register(Forum, ForumAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
