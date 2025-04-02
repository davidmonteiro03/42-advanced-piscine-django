from django import forms

class RegistrationForm(forms.Form):
    user_name = forms.CharField()
