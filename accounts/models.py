from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    return 'accounts/{0}'.format(filename,)


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    patronymic = models.CharField(
        verbose_name="Отчество",
        max_length=250,
        blank=True,
        null=True
    )
    photo = models.ImageField(
        verbose_name="Фотография пользователя",
        upload_to=user_directory_path,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.email
