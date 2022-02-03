from django import forms

class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email:')
        