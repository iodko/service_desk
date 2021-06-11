from django.contrib.auth import get_user_model
from django.db import models

from accounts.models import Organization, Subdivision
from attachments.models import Attachment
from contracts.models import Agreement

User = get_user_model()


class TicketCritical(models.TextChoices):
    """Набор степеней критичности заявки"""

    MINIMUM = "Минимальная"
    AVERAGE = "Обычная"
    HIGH = "Высокая"
    MAXIMUM = "Максимальная"
    BLOCKING = "Блокирующая"


class Ticket(models.Model):
    """Заявка от пользователя"""

    title = models.CharField(max_length=250, verbose_name="Заголовок")
    content = models.CharField(max_length=8000, verbose_name="Содержание")
    critical = models.CharField(
        max_length=250,
        choices=TicketCritical.choices,
        default=TicketCritical.MINIMUM,
        verbose_name="Критичность заявки",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    deadline = models.DateTimeField(
        "Максимальная дата решения", blank=True, null=True
    )
    finished_at = models.DateTimeField("Дата решения", blank=True, null=True)
    parent_id = models.ForeignKey(
        "Ticket", on_delete=models.PROTECT, verbose_name="Родительская заявка"
    )
    author = models.ForeignKey(
        User,
        related_name="tickets",
        on_delete=models.PROTECT,
        verbose_name="Автор",
    )
    responsible = models.ForeignKey(
        User,
        related_name="trust_tickets",
        verbose_name="Ответственный",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    service = models.ForeignKey(
        "Service",
        on_delete=models.PROTECT,
        related_name="tickets",
        verbose_name="Услуга",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        related_name="tickets",
        verbose_name="Категория",
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="tickets",
        verbose_name="Организация",
    )
    subdivision = models.ForeignKey(
        Subdivision,
        on_delete=models.PROTECT,
        related_name="tickets",
        verbose_name="Структурное подразделение",
    )
    status = models.ForeignKey(
        "Status",
        on_delete=models.PROTECT,
        related_name="tickets",
        verbose_name="Статус",
    )
    type = models.ForeignKey(
        "Type",
        on_delete=models.PROTECT,
        related_name="tickets",
        verbose_name="Тип заявки",
    )
    agreement = models.ForeignKey(
        Agreement,
        on_delete=models.PROTECT,
        related_name="tickets",
        verbose_name="Соглашение",
    )
    files = models.ManyToManyField(
        Attachment, related_name="tickets", verbose_name="Файлы"
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка №{self.id}"


class Status(models.Model):
    """Статус заявки"""

    name = models.CharField(max_length=250, verbose_name="Название статуса")

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return {self.name}


class AvailableStatus(models.Model):
    """
    Набор доступных статусов в зависимости от:
    - типа заявки
    - текущего статуса заявки
    """

    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name="available",
        verbose_name="Статус заявки",
    )
    types = models.ManyToManyField(
        "Type", related_name="available", verbose_name="Типы заявки"
    )
    available_statuses = models.ManyToManyField(
        Status,
        related_name="avl_for_status_types",
        verbose_name="Доступные Статусы",
    )

    class Meta:
        verbose_name = "Доступные Статусы"
        verbose_name_plural = "Доступные Статусы"

    def __str__(self):
        return f"Статус: {self.status} <--Е статусы"


class Type(models.Model):
    """Тип заявки"""

    name = models.CharField(max_length=250, verbose_name="Название типа")

    class Meta:
        verbose_name = "Тип заявки"
        verbose_name_plural = "Типы заявки"

    def __str__(self):
        return {self.name}


class AvailableType(models.Model):
    """Набор доступных типов заявки в зависимости от соглашения"""

    agreement = models.ForeignKey(
        Agreement,
        on_delete=models.CASCADE,
        related_name="avl_types",
        verbose_name="Соглашение",
    )
    available_types = models.ManyToManyField(
        Type, related_name="avl_for_agreements", verbose_name="Доступные типы"
    )

    class Meta:
        verbose_name = "Доступные Статусы"
        verbose_name_plural = "Доступные Статусы"

    def __str__(self):
        return f"Соглашение: {self.agreement} <--Е типы"


class Service(models.Model):
    """Услуга для заявки"""

    name = models.CharField(max_length=250, verbose_name="Название услуги")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return {self.name}


class AvailableService(models.Model):
    """
    Набор доступных улуг для заявки в зависимости от:
    - типа заявки
     - соглашения в заявке
    """

    agreement = models.ForeignKey(
        Agreement,
        on_delete=models.CASCADE,
        related_name="services",
        verbose_name="Соглашение",
    )
    type = models.ForeignKey(
        "Type",
        on_delete=models.CASCADE,
        related_name="services",
        verbose_name="Тип заявки",
    )

    available_services = models.ManyToManyField(
        Service,
        related_name="avl_for_agreements_types",
        verbose_name="Доступные типы",
    )

    class Meta:
        verbose_name = "Доступные Статусы"
        verbose_name_plural = "Доступные Статусы"

    def __str__(self):
        return f"{self.agreement} + {self.type}<--Е услуги"


class Category(models.Model):
    """Категория заявки"""

    name = models.CharField(max_length=250, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return {self.name}


class AvailableCategory(models.Model):
    """Набор доступных для заявки категорий в зависимости от соглашения"""

    agreement = models.ForeignKey(
        Agreement,
        on_delete=models.CASCADE,
        related_name="avl_categories",
        verbose_name="Соглашение",
    )

    available_categories = models.ManyToManyField(
        Service,
        related_name="avl_for_agreements",
        verbose_name="Доступные типы",
    )

    class Meta:
        verbose_name = "Доступные Категории"
        verbose_name_plural = "Доступные Категории"

    def __str__(self):
        return f"{self.agreement}<--Е категории"


class WorkDaysCount(models.Model):
    """Время до автоматического закрытия заявки после выполнения"""

    agreement = models.ForeignKey(
        Agreement, on_delete=models.CASCADE, verbose_name="Соглашение"
    )
    interval = models.DurationField(verbose_name="Время до закрытия")

    class Meta:
        verbose_name = "Время до закрытия"
        verbose_name_plural = "Время до закрытия"
