from django import forms
from .models import CodeSubmission
class CodeForm(forms.ModelForm):
    class Meta:
        model = CodeSubmission
        fields = ['code']