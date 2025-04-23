from django import forms
from django.contrib.auth.forms import AuthenticationForm
from control.models import Article, UserFavouriteArticle
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''
        self.fields['username'].widget.attrs.update({'placeholder': _('username')})
        self.fields['password'].widget.attrs.update({'placeholder': _('password')})


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "synopsis", "content"]
        labels = {'title': _("Title"),
                  'synopsis': _("Synopsis"),
                  'content': _("Content")}

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': _('title')})
        self.fields['synopsis'].widget.attrs.update({'placeholder': _('synopsis')})
        self.fields['content'].widget.attrs.update({'placeholder': _('content')})


class UserFavouriteArticleForm(forms.ModelForm):
    class Meta:
        model = UserFavouriteArticle
        fields = []
