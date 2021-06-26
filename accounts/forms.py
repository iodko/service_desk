from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import Select, TextInput
from django.shortcuts import get_object_or_404
from registration.forms import RegistrationForm
from django.utils.translation import gettext_lazy as _

from accounts.models import Organization

User = get_user_model()


class SignUpForm(RegistrationForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label='Имя'
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label='Фамилия'
    )
    patronymic = forms.CharField(
        max_length=150,
        required=True,
        label='Отчество'
    )

    organization = forms.CharField(
        max_length=300,
        label='Организация',
        widget=TextInput(attrs={
            'class': 'autocomplete',
            'data - error': "Please enter your first name."
        })
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'patronymic',
            'username',
            'email',
            'organization',
            'photo',
        )

    def clean_organization(self):
        name = self.cleaned_data['organization']
        if not Organization.objects.filter(name=name).exists():
            raise ValidationError("Нам не известно о такой организации")
        return get_object_or_404(Organization, name=name)

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.save()
        user.organizations.add(self.cleaned_data['organization'])
        return user
