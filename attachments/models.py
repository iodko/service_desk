from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Attachment(models.Model):
    """Модель представления Файла (хранит файлы новостей и заявок)"""

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="files",
        verbose_name="Автор",
    )
    file = models.FileField(
        upload_to="user_files/%Y/%m/%d/", verbose_name=" айл"
    )
    is_private = models.BooleanField(default=False, verbose_name="Приватность")
