from django.contrib import admin

from .models import Post
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ['__unicode__','timestamp','updated']
    search_fields = ['content','title']
    class Meta:

        model=Post


admin.site.register(Post,PostAdmin)
