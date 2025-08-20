from django.contrib import admin
from .models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'is_featured', 'status', 'created_at')
    list_filter = ('is_featured', 'status', 'created_at')
    search_fields = ('title', 'author_name', 'summary', 'body')

    # ✅ mark system fields as read-only
    readonly_fields = ('slug', 'created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('title', 'author_name', 'summary', 'body', 'cover', 'category')
        }),
        ('Publishing', {
            'fields': ('status', 'is_featured', 'published_at', 'word_file')
        }),
        ('System Info', {
            'fields': ('slug', 'views', 'created_at', 'updated_at'),
        }),
    )
