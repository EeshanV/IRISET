from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'content', 'file']
    list_filter = ['user']
    search_fields = ['title']


admin.site.register(Post,PostAdmin)