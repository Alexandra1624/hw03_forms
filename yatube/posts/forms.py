from django import forms
# from django.forms import ModelForm
from posts.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['group', 'text']
        labels = {
            'text': 'Текст поста',
            'group': 'Группа'}
        help_texts = {
            'text': 'Текст нового поста',
            'group': 'Группа, к которой будет относиться пост'}
