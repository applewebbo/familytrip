import pytest
from accounts.forms import ProfileForm
from accounts.tests.factories import CustomUserFactory


@pytest.mark.parametrize(
    "first_name, last_name, validity",
    [
        ("John", "Smith", True),
        ("John", "", False),
        ("", "Smith", False),
    ],
)
def test_profileform(first_name, last_name, validity):
    user = CustomUserFactory()
    form = ProfileForm(data={"first_name": first_name, "last_name": last_name}, pk=user.pk)

    assert form.is_valid() is validity
