from django.shortcuts import render
from mysite import settings

# Create your views here.
def helloworld(request):
    return render(request, settings.BASE_DIR / 'helloworld' / 'templates' / 'helloworld.html')
