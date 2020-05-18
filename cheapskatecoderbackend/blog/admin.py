from django.contrib import admin
from blog.models import *


class BlogAdmin(admin.ModelAdmin):
    raw_id_fields = ['author']
    filter_horizontal = ['series', 'categories']
    fields = ['title', 'slug', 'meta_summary', 'blog_content', 'author', 'is_published',
    'date_published', 'date_updated', 'date_saved_draft', 'series', 'categories']
    readonly_fields = ['date_published', 'date_updated', 'date_saved_draft']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Series)
admin.site.register(Category)