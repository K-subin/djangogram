from django import forms
from .models import Post
from .widgets import PreviewFileWidget

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'text',)
        widgets = {
            'image' : PreviewFileWidget,
        }