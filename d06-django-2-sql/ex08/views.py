from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.conf import settings

# Create your views here.
def init(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""\
CREATE TABLE IF NOT EXISTS ex08_planets(
id SERIAL PRIMARY KEY,
name VARCHAR(64) UNIQUE NOT NULL,
climate VARCHAR,
diameter INTEGER,
orbital_period INTEGER,
population BIGINT,
rotation_period INTEGER,
surface_water REAL,
terrain VARCHAR(128));""")
            cursor.execute("""\
CREATE TABLE IF NOT EXISTS ex08_people(
id SERIAL PRIMARY KEY,
name VARCHAR(64) UNIQUE NOT NULL,
birth_year VARCHAR(32),
gender VARCHAR(32),
eye_color VARCHAR(32),
hair_color VARCHAR(32),
height INTEGER,
mass REAL,
homeworld VARCHAR(64) REFERENCES ex08_planets(name));""")
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)


def read_csv(file_path, table_name):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM {table_name};""".format(table_name=table_name))
        columns = ", ".join([desc.name for desc in cursor.description if desc.name != 'id'])
        with open(file_path, 'r') as file:
            cursor.copy_expert("""\
COPY {table_name} ({columns}) FROM STDIN WITH (FORMAT CSV, DELIMITER E'\\t', HEADER FALSE, NULL 'NULL');""".format(table_name=table_name, columns=columns), file)


def populate(request):
    try:
        read_csv(settings.BASE_DIR / 'ex08' / 'planets.csv', 'ex08_planets')
        read_csv(settings.BASE_DIR / 'ex08' / 'people.csv', 'ex08_people')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)


def display(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""\
SELECT ex08_people.name, ex08_people.homeworld, ex08_planets.climate FROM ex08_people
JOIN ex08_planets ON ex08_people.homeworld=ex08_planets.name
WHERE ex08_planets.climate LIKE '%windy%'
ORDER BY ex08_people.name;""")
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
        return render(request, 'ex08/display.html', context={'columns': columns,
                                                             'results': results})
    except:
        return HttpResponse("No data available")
