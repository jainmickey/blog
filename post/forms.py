from django import forms
from django.forms import ModelForm

from post.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
    #title = forms.CharField(max_length=300)
    #body = forms.CharField(widget=forms.Textarea)
    #date = forms.DateField(initial=datetime.date.today)
    #tags = forms.CharField(max_length=50)

