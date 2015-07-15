from django import forms

from crispy_forms.helper import FormHelper

class NewAdventureForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.fields.TextInput(attrs={
            'placeholder': 'The Mysterious Quest',
            'class': 'form-control input-lg',
            'id': 'id_adventure_title'
        }),
        error_messages={
            'required': 'Your adventure needs a title!'
        }
    )
