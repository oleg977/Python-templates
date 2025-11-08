# myapp/models.py

from django.db import models


class Item(models.Model):
    """Базовая модель для демонстрации CRUD-операций."""

    name = models.CharField(max_length=100, verbose_name="Название предмета")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
        ordering = ["-created_at"]  # Сортировка по дате создания (новые сверху)

    def __str__(self):
        return self.name
