from accounts.tests.factories import (
    CustomUserFactory,
    ProfileFactory,
    TravelFriendFactory,
)


class TestCustomUser:
    def test_factory(self):
        """The factory produces a valid instance and related user_profile"""
        user = CustomUserFactory()

        assert user is not None
        assert str(user) is user.email
        assert user.profile is not None


class TestProfile:
    def test_profile(self):
        """The profile is connected to a user and holds user state"""
        profile = ProfileFactory()

        assert profile is not None
        assert str(profile) == profile.user.email
        assert profile.user is not None
        assert profile.status == profile.Status.TRIAL


class TestTravelFriend:
    def test_travelfriend(self):
        """The family member is connected to a user and have valid attributes"""

        travel_friend = TravelFriendFactory()

        assert travel_friend is not None
        assert str(travel_friend) == travel_friend.name
        assert travel_friend.user is not None
        assert travel_friend.name is not None
        assert travel_friend.birthdate is not None
