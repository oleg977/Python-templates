# myapp/tests.py

from django.test import TestCase
from django.urls import reverse

# Создаем базовый класс для тестирования представлений
class AppViewTests(TestCase):

    def test_home_page_status_code(self):
        """Тест: Главная страница доступна (код 200)."""
        # Проверяем, что представление, связанное с именем 'index', возвращает код 200
        response = self.client.get(reverse('myapp:index'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        """Тест: Страница 'О нас' доступна."""
        response = self.client.get(reverse('myapp:about'))
        self.assertEqual(response.status_code, 200)

    # Здесь можно добавить тесты для форм, моделей и логики.