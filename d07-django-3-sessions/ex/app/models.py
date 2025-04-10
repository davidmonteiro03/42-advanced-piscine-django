from django.db import models
from django.contrib.auth.models import User


class Tip(models.Model):
    content = models.TextField(verbose_name='content',
                               blank=False,
                               null=False)
    author = models.ForeignKey(to=User,
                               on_delete=models.CASCADE,
                               editable=False)
    date = models.DateField(verbose_name='content',
                            auto_now_add=True,
                            blank=False,
                            null=False,
                            editable=False)