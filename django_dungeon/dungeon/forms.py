from django.forms import ModelForm, TextInput, CharField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Adventure

class NewAdventureForm(ModelForm):
    class Meta:
        model = Adventure
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'The Mysterious Quest',
                'class': 'form-control input-lg',
                'id': 'id_adventure_title',
            })
        }
        error_messages = {
            'title': {
                'required': 'Your adventure needs a title!'
            }
        }


    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('create', 'create', css_class='btn-primary', css_id='id_save_button'))