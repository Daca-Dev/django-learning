from django.contrib import admin
from .models import Post, Comment


# registro del modelo de Post en el panel de admin de Django
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # vista de lista
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # por cada post
    #? define what fields going to be completed based on other filds
    prepopulated_fields = {'slug': ('title',)}
    #? define that the author is selecte in and separated window that launch when
    #? you click on it
    raw_id_fields = ('author',)
    # general
    #? define the post in the panel admin by categories that created based on publish field
    #? this atribute should use a datetime field
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')