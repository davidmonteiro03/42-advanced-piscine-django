from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def init(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""\
CREATE TABLE IF NOT EXISTS ex06_movies(
title VARCHAR(64) UNIQUE NOT NULL,
episode_nb INTEGER PRIMARY KEY,
opening_crawl TEXT,
director VARCHAR(32) NOT NULL,
producer VARCHAR(128) NOT NULL,
release_date DATE NOT NULL,
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL);""")
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)


def populate(request):
    try:
        with connection.cursor() as cursor:
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
            output = ""
            for ep in episodes:
                try:
                    cursor.execute("""\
INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date) \
VALUES (%(episode_nb)s, %(title)s, %(director)s, %(producer)s, %(release_date)s);""", ep)
                    output += "OK<br>"
                except Exception as e:
                    output += str(e) + "<br>"
        return HttpResponse(output)
    except Exception as e:
        return HttpResponse(e)


def display(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM ex06_movies ORDER BY episode_nb;""")
            columns = [desc[0] for desc in cursor.description]
            fetched = cursor.fetchall()
            if len(fetched) < 1:
                return HttpResponse("No data available")
            results = []
            for _ in fetched:
                _dict = {}
                for __ in range(len(columns)):
                    _dict[columns[__]] = _[__]
                results.append(_dict)
        return render(request, 'ex06/display.html', context={'columns': columns,
                                                             'results': results})
    except:
        return HttpResponse("No data available")


def update(request):
    if request.method == 'POST':
        try:
            with connection.cursor() as cursor:
                cursor.execute("""\
UPDATE ex06_movies \
SET opening_crawl=%s \
WHERE episode_nb=%s;""", [request.POST['opening_crawl'], request.POST['episode_nb']])
        except:
            pass
        return redirect('/ex06/update')
    try:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM ex06_movies ORDER BY episode_nb;""")
            columns = [desc[0] for desc in cursor.description]
            fetched = cursor.fetchall()
            if len(fetched) < 1:
                return HttpResponse("No data available")
            results = []
            for _ in fetched:
                _dict = {}
                for __ in range(len(columns)):
                    _dict[columns[__]] = _[__]
                results.append(_dict)
        return render(request, 'ex06/update.html', context={'results': results})
    except:
        return HttpResponse("No data available")
