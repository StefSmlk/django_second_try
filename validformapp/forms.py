from django import forms
from django.core import validators


def check_for_a(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError('Make needs to start with "a"')

class NameForm(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your e-mail again")
    text = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(5)])

    def clean(self):
        clean_data = super().clean()
        email = clean_data['email']
        vmail = clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError('Make shure email match')
        return clean_data
