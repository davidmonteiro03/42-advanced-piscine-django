from django.shortcuts import render, redirect
from . import forms
import logging
from django.conf import settings

# Create your views here.
def index(request):
    history_logs = logging.getLogger('history')
    if request.method == 'POST':
        form = forms.History(request.POST)
        if form.is_valid():
            history_logs.info(form.cleaned_data['history'])
        return redirect('/ex02')
    try:
        f = open(settings.HISTORY_LOG_FILE, 'r')
        history = [line.strip() for line in f.readlines()]
        f.close()
    except:
        history = []
    print(history)
    return render(request, 'ex02/index.html', context={'form': forms.History(), 'history': history})
