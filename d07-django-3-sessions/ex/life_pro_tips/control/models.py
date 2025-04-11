from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    can_downvote_tips = models.BooleanField(verbose_name='downvote permission',
                                            blank=False,
                                            null=False,
                                            default=False)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.can_downvote_tips = True
        super().save(*args, **kwargs)


class Tip(models.Model):
    content = models.TextField(verbose_name='content',
                               blank=False,
                               null=False)
    author = models.ForeignKey(to=CustomUser,
                               on_delete=models.CASCADE,
                               editable=False)
    date = models.DateField(verbose_name='date',
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
