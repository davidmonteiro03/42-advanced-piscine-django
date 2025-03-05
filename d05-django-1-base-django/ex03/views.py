from django.shortcuts import render

# Create your views here.
def index(request):
    colors = {'noir': 'black',
              'rouge': 'red',
              'bleu': 'blue',
              'vert': 'green'}
    return render(request,
                  'ex03/index.html',
                  context={'colors': colors.keys(),
                           'lines': [[{'color': __} for __ in colors.values()]
                                     for _ in range(50)]})
