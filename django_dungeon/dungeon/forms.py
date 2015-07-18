from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

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

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('create', 'create', css_class='btn-primary', css_id='id_save_button'))