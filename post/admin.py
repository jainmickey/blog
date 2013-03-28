from django.contrib import admin
from post.models import Post, Tags, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('published', 'title', 'body')
    fields = ('published', 'title', 'slug', 'body', 'tags', 'category', 'author')
    date_hierarchy = "date"
    list_display_links = ["title"]
    list_editable = ["published"]
    list_filter = ["published", "date", "author"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "content"]

admin.site.register(Post, PostAdmin)
admin.site.register(Tags)
admin.site.register(Category)
