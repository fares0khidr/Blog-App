from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Post


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'tags', 'published')
