from django.forms import ModelForm, Textarea
from .models import *

class DoctorRegister(ModelForm):
    class Meta:
        model = patient
        fields = '__all__'
        labels = {
            'first_name': 'First Name'
        }
        help_texts = {
            'first_name': 'Some useful help text.'
        }
        error_messages = {
            'first_name': {
                'max_length': "This writer's name is too long."
            },
        }
