from django.urls import re_path, path
from control.views import Articles, Home, Login, Publications, Detail, Logout, Favourites


urlpatterns = [
    re_path(r'^articles/?$', Articles.as_view(), name='articles'),
    path('', Home.as_view(), name='home'),
    re_path(r'^login/?$', Login.as_view(), name='login'),
    re_path(r'^publications/?$', Publications.as_view(), name='publications'),
    re_path(r'^detail/(?P<pk>\d+)/?$', Detail.as_view(), name='detail'),
    re_path(r'^logout/?$', Logout.as_view(), name='logout'),
    re_path(r'^favourites/?$', Favourites.as_view(), name='favourites'),
]
