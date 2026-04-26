from django import forms
from .models import blog

class blogform(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title' ,'summary','slug', 'content','published_date','is_published']