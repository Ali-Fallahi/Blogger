
from django import forms
from . models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image', 'title', 'slug', 'category', 'body']
