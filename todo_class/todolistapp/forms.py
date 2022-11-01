from .models import Tasktable
from django import forms

class todoform(forms.ModelForm):
    class Meta:
        model=Tasktable
        fields=['name','priority','date']
