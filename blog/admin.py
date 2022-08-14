from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    raw_id_fields = ('likes',)
    search_fields = ('title', 'author__username', 'published_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text')
    raw_id_fields = ('author',)
    search_fields = ('post__title', 'author__username')


admin.site.register(Tag)
