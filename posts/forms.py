import os

from django import forms
from django.core.exceptions import ValidationError


from .models import Post


from django.core.validators import MaxLengthValidator



class PostForm(forms.ModelForm):

    title=forms.CharField(min_length=40)

    content=forms.TextInput()

    class Meta:
        model=Post
        fields=[
            "title",

            "content",
            "fimage",
        ]

