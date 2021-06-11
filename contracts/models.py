from django.db import models


class Contract(models.Model):
    number = models.CharField(
        verbose_name="Номер договора",
        max_length=250
    )


class Agreement(models.Model):
    name = models.CharField(
        verbose_name="Наименование соглашения",
        max_length=250
    )
