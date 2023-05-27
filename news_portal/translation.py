from .models import Category, Post
from modeltranslation.translator import register, TranslationOptions


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name_category', )


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('header', 'text_post', 'post_rating', )
