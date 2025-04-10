from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Tip(models.Model):
    content = models.TextField(verbose_name='content',
                               blank=False,
                               null=False)
    author = models.ForeignKey(to=CustomUser,
                               on_delete=models.CASCADE,
                               editable=False)
    date = models.DateField(verbose_name='content',
                            auto_now_add=True,
                            blank=False,
                            null=False,
                            editable=False)
    upvotes = models.ManyToManyField(to=CustomUser,
                                     related_name='upvote_author',
                                     blank=True,
                                     editable=False)
    downvotes = models.ManyToManyField(to=CustomUser,
                                       related_name='downvote_author',
                                       blank=True,
                                       editable=False)