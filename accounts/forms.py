from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Submit
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.urls import reverse_lazy

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name")

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop("pk")
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {
            "hx-post": reverse_lazy("accounts:profile_edit", kwargs={"pk": self.pk}),
        }
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            FloatingField("first_name"),
            FloatingField("last_name"),
            Div(
                Submit("submit", "Salva"),
                css_class="d-grid",
            ),
        )
