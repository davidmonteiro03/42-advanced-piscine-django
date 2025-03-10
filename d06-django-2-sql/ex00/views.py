from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def init(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
CREATE TABLE IF NOT EXISTS ex00_movies(
    title VARCHAR(64) UNIQUE NOT NULL,
    episode_nb INTEGER PRIMARY KEY,
    opening_crawl TEXT,
    director VARCHAR(32) NOT NULL,
    producer VARCHAR(128) NOT NULL,
    release_date DATE NOT NULL
)""")
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)
