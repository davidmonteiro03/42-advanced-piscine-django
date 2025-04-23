from django.urls import re_path, path
from control.views import Articles, Home, Login, Publications, Detail, Logout, Favourites, Register, Publish, AddToFavourite


urlpatterns = [
    re_path(r'^articles/?$', Articles.as_view(), name='articles'),
    path('', Home.as_view(), name='home'),
    re_path(r'^login/?$', Login.as_view(), name='login'),
    re_path(r'^publications/?$', Publications.as_view(), name='publications'),
    re_path(r'^detail/(?P<pk>\d+)/?$', Detail.as_view(), name='detail'),
    re_path(r'^logout/?$', Logout.as_view(), name='logout'),
    re_path(r'^favourites/?$', Favourites.as_view(), name='favourites'),
    re_path(r'^register/?$', Register.as_view(), name='register'),
    re_path(r'^publish/?$', Publish.as_view(), name='publish'),
    re_path(r'^add_to_favourite/(?P<pk>\d+)/?$', AddToFavourite.as_view(), name='add_to_favourite'),
]
