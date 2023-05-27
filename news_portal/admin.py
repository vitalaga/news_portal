from django.contrib import admin
from .models import Post, Author, Category, Comment
from modeltranslation.admin import TranslationAdmin


class CategoryAdminTranslation(TranslationAdmin):
    model = Category


class PostAdminTranslation(TranslationAdmin):
    model = Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'object_type', 'date_post', 'header', 'preview', 'post_rating']
    list_filter = ['date_post', 'object_type', 'post_rating']
    search_fields = ['name', 'category__name_category']


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)

