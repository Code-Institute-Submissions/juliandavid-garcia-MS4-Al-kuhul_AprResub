from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		exclude = ('user',)
		fields = ['name', 'email', 'body',]


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		exclude = ('user',)
		fields = ('title', 'slug', 'author', 'content', 'status')

	