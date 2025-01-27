from django import forms
from .models import TranslatedText

class TranslatedTextForm(forms.ModelForm):
    class Meta:
        model = TranslatedText
        fields = ['original_text', 'translated_en', 'translated_ar']
        widgets = {
            'original_text': forms.Textarea(attrs={'rows': 4, 'class': 'vLargeTextField'}),
            'translated_en': forms.Textarea(attrs={'rows': 4, 'class': 'vLargeTextField'}),
            'translated_ar': forms.Textarea(attrs={'rows': 4, 'class': 'vLargeTextField'}),
        }
