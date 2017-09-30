from django import forms

from .models import Post


# class PostCreateForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField(widget=forms.Textarea, required=False)



class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content'
        ]