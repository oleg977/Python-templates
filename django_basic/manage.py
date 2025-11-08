# manage.py

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# ⬅️ ИЗМЕНЕНИЯ ЗДЕСЬ ⬅️
# Добавьте эти строки, чтобы корневая папка (где лежит manage.py)
# всегда была в Python Path.
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# ---------------------

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings') # ⬅️ Установите здесь (вместо env:)
    try:
        from django.core.management import execute_from_command_line
    # ...
# ...