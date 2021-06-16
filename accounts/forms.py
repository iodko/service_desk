from django import forms
from django.contrib.auth import get_user_model
from registration.forms import RegistrationForm

User = get_user_model()


class SignUpForm(RegistrationForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
    )
    patronymic = forms.CharField(
        max_length=150,
        required=True,
        label='Отчество'
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'patronymic',
            'username',
            'email',
            'organizations',
            'photo',
        )
        help_texts = {
            "username": (
                "<ul><li>Не более 150 символов.</li>"
                "<li>Только буквы, цифры и символы "
                "@/./+/-/_.</li></ul>"
            ),
        }
