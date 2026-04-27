from django import forms
from .models import Blog

class blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title' ,'summary','slug', 'content','published_date','is_published']