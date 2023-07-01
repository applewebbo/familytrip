from accounts.tests.factories import CustomUserFactory


class TestCustomUser:
    def test_factory(self):
        """The factory produces a valid instance"""
        user = CustomUserFactory()

        assert user is not None
