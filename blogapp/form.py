from django import forms
from .models import Blog

class BlogPost(forms.ModelForm): # Model 기반의 입력공간
    class Meta: # meta class: inner class
        model = Blog
        fields = ['title', 'body']

# Other form fields for practice
'''
class BlogPost(forms.Form): # 임의의 입력공간
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[('1','one'), ('2','two'), ('3','three')])
'''