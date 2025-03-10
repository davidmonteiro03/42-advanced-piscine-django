from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .models import Movies

# Create your views here.
def populate(request):
    try:
        episodes = [
            {
                'episode_nb': 1,
                'title': "The Phantom Menace",
                'director': "George Lucas",
                'producer': "Rick McCallum",
                'release_date': "1999-05-19",
            },
            {
                'episode_nb': 2,
                'title': "Attack of the Clones",
                'director': "George Lucas",
                'producer': "Rick McCallum",
                'release_date': "2002-05-16",
            },
            {
                'episode_nb': 3,
                'title': "Revenge of the Sith",
                'director': "George Lucas",
                'producer': "Rick McCallum",
                'release_date': "2005-05-19",
            },
            {
                'episode_nb': 4,
                'title': "A New Hope",
                'director': "George Lucas",
                'producer': "Gary Kurtz, Rick McCallum",
                'release_date': "1977-05-25",
            },
            {
                'episode_nb': 5,
                'title': "The Empire Strikes Back",
                'director': "Irvin Kershner",
                'producer': "Gary Kurtz, Rick McCallum",
                'release_date': "1980-05-17",
            },
            {
                'episode_nb': 6,
                'title': "Return of the Jedi",
                'director': "Richard Marquand",
                'producer': "Howard G. Kazanjian, George Lucas, Rick McCallum",
                'release_date': "1983-05-25",
            },
            {
                'episode_nb': 7,
                'title': "The Force Awakens",
                'director': "J. J. Abrams",
                'producer': "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
                'release_date': "2015-12-11",
            },
        ]
        for ep in episodes:
            Movies.objects.create(**ep)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)


def display(request):
    try:
        fetched = Movies.objects.all()
        columns = [_.name for _ in list(Movies._meta.fields)]
        results = []
        for _ in fetched:
            _dict = {}
            for __ in columns:
                _dict[__] = _.__dict__.get(__)
            results.append(_dict)
        if len(results) < 1:
            return HttpResponse("No data available")
        return render(request, 'ex05/display.html', context={'columns': columns,
                                                             'results': results})
    except:
        return HttpResponse("No data available")


def remove(request):
    if request.method == 'POST':
        try:
            Movies.objects.filter(episode_nb=request.POST['episode_nb']).first().delete()
        except:
            pass
        return redirect('/ex05/remove')
    try:
        fetched = Movies.objects.all()
        results = [model_to_dict(_) for _ in fetched]
        if len(results) < 1:
            return HttpResponse("No data available")
        return render(request, 'ex05/remove.html', context={'results': results})
    except:
        return HttpResponse("No data available")
