from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {'content': forms.Textarea(attrs={'cols':80})}

