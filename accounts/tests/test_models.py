from accounts.tests.factories import (
    CustomUserFactory,
    FamilyMemberFactory,
    ProfileFactory,
)


class TestCustomUser:
    def test_factory(self):
        """The factory produces a valid instance"""
        user = CustomUserFactory()

        assert user is not None
        assert str(user) is user.email
        assert user.profile is not None


class TestProfile:
    def test_profile(self):
        """The profile is connected to a user and holds user state"""
        profile = ProfileFactory()

        assert profile is not None
        assert profile.user is not None
        assert profile.status == profile.Status.TRIAL


class TestFamilyMember:
    def test_familymember(self):
        """The family member is connected to a user and have valid attributes"""

        family_member = FamilyMemberFactory()

        assert family_member is not None
        assert family_member.user is not None
        assert family_member.name is not None
        assert family_member.birthdate is not None
