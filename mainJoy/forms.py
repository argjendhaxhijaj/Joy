from django import forms
from .models import njoftimet

class PostForm(forms.ModelForm):

    class Meta:
        model = njoftimet
        #fields = 'first_name', 'last_name','title','content','upload'
        fields = ('first_name','last_name','title','content','document','url')
        