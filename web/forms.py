from django import forms
from web.models import Word

class WordSubmissionForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['content']
        
