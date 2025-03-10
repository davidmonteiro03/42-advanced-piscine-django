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


def read_planets_csv(file_path, exclude):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM ex08_planets;""")
        keys = [desc.name for desc in cursor.description if desc.name not in exclude]
        with open(file_path, 'r') as file:
            for line in file.readlines():
                values = line.strip().split()
                _dict = {}
                for k, v in zip(keys, values):
                    _dict[k] = v


def populate(request):
    try:
        read_planets_csv(settings.BASE_DIR / 'ex08' / 'planets.csv', ['id'])
        # read_people_csv(settings.BASE_DIR / 'ex08' / 'people.csv')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)
