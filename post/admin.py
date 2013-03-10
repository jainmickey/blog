from django.contrib import admin
from post.models import Post, Tags, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Post, PostAdmin)
admin.site.register(Tags)
admin.site.register(Category)
