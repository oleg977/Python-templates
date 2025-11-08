# myapp/forms.py

from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """Форма, созданная на основе модели Item."""

    class Meta:
        model = Item
        # Указываем, какие поля будут отображаться в форме
        fields = ("name", "description", "is_active")

        # Добавляем классы Bootstrap для стилизации полей
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            # is_active не нуждается в кастомном классе, так как это Checkbox
        }
