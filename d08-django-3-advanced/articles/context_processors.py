from control.forms import LoginForm
from articles.settings import LANGUAGES

def login_form(request):
    return {'login_form': LoginForm}


def languages(request):
    return {'LANGUAGES': dict(LANGUAGES)}
