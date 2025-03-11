from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import People, MoviesCharacters
from datetime import datetime

# Create your views here.
def index(request):
    characters = People.objects.all()
    genders = []
    for c in characters:
        if c.gender in genders:
            continue
        genders.append(c.gender)
    if request.GET:
        try:
            movies_minimum_release_date = datetime.strptime(request.GET['movies_minimum_release_date'], "%Y-%m-%d").date()
            movies_maximum_release_date = datetime.strptime(request.GET['movies_maximum_release_date'], "%Y-%m-%d").date()
            planet_diameter_greater_than = int(request.GET['planet_diameter_greater_than'])
            character_gender = str(request.GET['character_gender'])
            movies_chars = MoviesCharacters.objects.all()
            results = []
            for _ in movies_chars:
                try:
                    matched = \
                        _.character.gender == character_gender and \
                        (_.movie.release_date > movies_minimum_release_date and \
                         _.movie.release_date < movies_maximum_release_date) and \
                        _.character.homeworld.diameter >= planet_diameter_greater_than
                    if matched is not True:
                        continue
                    results.append({'character_name': _.character.name,
                                    'character_gender': _.character.gender,
                                    'movie_title': _.movie.title,
                                    'homeworld_name': _.character.homeworld.name,
                                    'homeworld_diameter': _.character.homeworld.diameter})
                except:
                    continue
            if len(results) < 1:
                return HttpResponse("Nothing corresponding to your research")
            return render(request, 'ex10/index.html', context={'genders': genders,
                                                               'results': results})
        except:
            return redirect('/ex10')
    return render(request, 'ex10/index.html', context={'genders': genders})
