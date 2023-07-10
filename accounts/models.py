from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.email


class Profile(models.Model):
    """Profile holds user informations not related to auth"""

    class Status(models.IntegerChoices):
        EXEMPT = 1  # for special users that requires no subscription
        BETA = 2  # for beta users
        TRIAL = 3
        ACTIVE = 4
        CANCELLED = 5
        TRIAL_EXPIRED = 6

    ACTIVE_STATUSES = (Status.ACTIVE, Status.TRIAL, Status.EXEMPT)

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
    )
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.TRIAL,
        db_index=True,
    )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    """A new user get an associated profile"""
    if created:
        Profile.objects.create(user=instance)
