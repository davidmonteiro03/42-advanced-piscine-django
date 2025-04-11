from django.db import models
from django.contrib.auth.models import AbstractUser
import life_pro_tips.settings as settings


class CustomUser(AbstractUser):
    can_downvote_tips = models.BooleanField(verbose_name='downvote permission',
                                            blank=False,
                                            null=False,
                                            default=False)
    rep_points = models.BigIntegerField(verbose_name='reputation points',
                                        blank=False,
                                        null=False,
                                        default=0)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            self_tips = Tip.objects.filter(author=self).all()
            rep_points = 0
            for st in self_tips:
                rep_points += len(st.upvotes.all()) * settings.REP_POINTS_PER_UPVOTE_TIP
                rep_points -= len(st.downvotes.all()) * settings.REP_POINTS_PER_DOWNVOTE_TIP
            self.rep_points = rep_points
        self.can_downvote_tips = self.is_superuser or self.rep_points >= settings.REP_POINTS_TO_DOWNVOTE_TIPS
        self.is_staff = self.is_superuser or self.rep_points >= settings.REP_POINTS_TO_DELETE_TIPS
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
