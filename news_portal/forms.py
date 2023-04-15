from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'author',
            'header',
            'text_post',
            'categories',
        ]

    def clean(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get("header")
        text_post = cleaned_data.get("text_post")
        if heading == text_post:
            raise ValidationError("Описание не должно быть идентично названию.")
        return cleaned_data
