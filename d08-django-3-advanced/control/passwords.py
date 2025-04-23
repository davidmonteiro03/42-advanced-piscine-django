from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

users = User.objects.all()

for u in users:
    u.password = make_password(password='secret')
    u.save()
