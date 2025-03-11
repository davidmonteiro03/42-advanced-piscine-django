from django.shortcuts import render
from django.http import HttpResponse
from .models import People

# Create your views here.
def display(request):
    init_data_cmd = "python manage.py loaddata ex09/ex09_initial_data.json"
    try:
        people = People.objects.all().order_by('name')
        columns = ['name', 'homeworld', 'climate']
        results = []
        for p in people:
            if p.homeworld is None:
                continue
            if p.homeworld.climate is None:
                continue
            if p.homeworld.climate.find("windy") == -1:
                continue
            results.append({'name': str(p),
                            'homeworld': str(p.homeworld),
                            'climate': str(p.homeworld.climate)})
        if len(results) < 1:
            return HttpResponse(f"No data available, please use the following command line before use: {init_data_cmd}")
        return render(request, 'ex09/display.html', context={'columns': columns,
                                                             'results': results})
    except:
        return HttpResponse(f"No data available, please use the following command line before use: {init_data_cmd}")
