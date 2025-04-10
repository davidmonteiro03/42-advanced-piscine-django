from django import forms
from .models import Tip


class RegistrationForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TipForm(forms.models.ModelForm):
    class Meta:
        model = Tip
        fields = "__all__"
