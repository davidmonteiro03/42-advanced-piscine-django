from django import forms
from django.contrib.auth.forms import AuthenticationForm
from control.models import Article, UserFavouriteArticle


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''
        self.fields['username'].widget.attrs.update({'placeholder': 'username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'password'})


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "synopsis", "content"]


class UserFavouriteArticleForm(forms.ModelForm):
    class Meta:
        model = UserFavouriteArticle
        fields = []
