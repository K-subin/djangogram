from django import forms

class PreviewFileWidget(forms.ClearableFileInput):
    template_name = "posts/post_create.html"
    class Meta:
        js = [
            "//code.jquery.com/jquery-3.4.1.min.js",
        ]