from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ('title', 'content', 'thumbnail',
        'categories', 'featured')
