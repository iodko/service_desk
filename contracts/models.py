from django.db import models

from accounts.models import Organization
from attachments.models import Attachment


def contract_directory_path(instance, filename):
    return f'contracts/{filename}'


class Agreement(models.Model):
    name = models.CharField(
        verbose_name="Наименование соглашения",
        max_length=250
    )

    class Meta:
        verbose_name = "Соглашение"
        verbose_name_plural = "Соглашения"

    def __str__(self):
        return self.name


class Contract(models.Model):
    number = models.CharField(
        verbose_name="Номер договора",
        max_length=250
    )
    organization = models.ForeignKey(
        Organization,
        verbose_name="Организация",
        on_delete=models.PROTECT,
        related_name="contracts"
    )
    file = models.FileField(
        verbose_name="Электронная версия договора",
        upload_to=contract_directory_path,
        blank=True,
        null=True
    )
    agreements = models.ManyToManyField(
        Agreement,
        related_name="agr_contracts",
        verbose_name="Соглашения"
    )
    start_date = models.DateField(
        verbose_name="Дата начала действия договора"
    )
    end_date = models.DateField(
        verbose_name="Дата окончания действия договора"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания")

    class Meta:
        verbose_name = "Договор"
        verbose_name_plural = "Договора"

    def __str__(self):
        return f"Договор №{self.number} от {self.start_date}"



