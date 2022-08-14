from django.contrib import admin
from blog.models import Post, Tag, Comment
from django.utils.safestring import mark_safe


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'author',
        'image',
        'preview',
        'text',
        'tags',
        'published_at',
        'likes'
    )
    list_display = ('title', 'author',)
    raw_id_fields = ('likes',)
    search_fields = ('title', 'author__username', 'published_at',)
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text')
    raw_id_fields = ('author',)
    search_fields = ('post__title', 'author__username')


admin.site.register(Tag)
