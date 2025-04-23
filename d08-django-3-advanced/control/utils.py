from django.http import HttpRequest
from django.utils import translation
from articles import settings


def update_language(request: HttpRequest) -> None:
    if not request.session.get('lang'):
        request.session['lang'] = settings.LANGUAGE_CODE
    translation.activate(request.session['lang'])
