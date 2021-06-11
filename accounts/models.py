from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    return 'accounts/users_photo/{0}'.format(filename,)


def org_directory_path(instance, filename):
    return 'accounts/org_photo/{0}'.format(filename,)


class Organization(models.Model):
    name = models.CharField(
        verbose_name="Наименование организации",
        max_length=250
    )
    photo = models.ImageField(
        verbose_name="Фотография",
        upload_to=user_directory_path,
        blank=True,
        null=True
    )
    inn = models.CharField(
        verbose_name="ИНН организации",
        max_length=12,
        blank=True,
        null=True
    )
    kpp = models.CharField(
        verbose_name="КПП организации",
        max_length=9,
        blank=True,
        null=True
    )

    class Meta:
        ordering = "name"
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name


class Subdivision(models.Model):
    name = models.CharField(
        verbose_name="Наименование подразделения",
        max_length=250
    )

    class Meta:
        ordering = "name"
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name


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
    OrganizationDetail = models.ManyToManyField(
        Organization,
        through='OrganizationDetail',
        related_name='staff'
    )

    def __str__(self):
        return self.email


class OrganizationDetail(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT
    )
    subdivision = models.ForeignKey(
        Subdivision,
        on_delete=models.PROTECT
    )
    is_accepted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Данные организации'
        verbose_name_plural = 'Данные организаций'
