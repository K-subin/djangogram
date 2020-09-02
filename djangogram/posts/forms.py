from django import forms
from .models import Post

class CreateForm(forms.ModelForm):  
    class Meta:
        model = Post
        fields = ['text', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].queryset = Post.objects.values_list('image')
        self.fields['image'].widget.attrs.update({'class':'realInput'})
        self.fields['image'].widget.attrs['onchange']='setThumbnail(event)'
