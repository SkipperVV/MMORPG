from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Author, Category, Post, Comment, PostCategory


class PostsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'post_time')
    list_filter = ('author', 'post_time')


# Регистрируем модели для перевода в админке
class PostAdmin(TranslationAdmin):
    model = Post


class CommentAdmin(TranslationAdmin):
    model = Comment


admin.site.register(Post, PostsAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostCategory)
