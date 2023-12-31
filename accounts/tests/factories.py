import factory
from django.db.models.signals import post_save


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "accounts.CustomUser"


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "accounts.Profile"

    user = factory.SubFactory("accounts.tests.factories.CustomUserFactory")


@factory.django.mute_signals(post_save)
class TravelFriendFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "accounts.TravelFriend"

    user = factory.SubFactory("accounts.tests.factories.CustomUserFactory")
    birthdate = factory.Faker(
        "date_of_birth",
        maximum_age=25,
    )
