# Основные команды Git

## Инициализация репозитория
```bash
git init

Проверка состояния
git status

Добавление файлов
git add <file_name>  # Добавить конкретный файл
git add .            # Добавить все файлы

Создание комминта
git commit -m "Commit message"

Создавать коммит конретно, вместо git add .
git add Python-templates/shoplist/git_basic/

История коммитов
git log

---

### 2. **Добавление файлов и коммиты**

Создайте файл `adding_and_committing.md`:

```markdown
# Добавление файлов и коммиты

## Добавление одного файла
```bash
git add new_shoplist/manage.py

Добавление изменений и новых файлов
git add .
Забыл добавить или изменить файл
git commit --amend

Удаление файла
git reset <file_name>

---

### 3. **Работа с удалённым репозиторием**

Создайте файл `remote_repository.md`:

```markdown
# Работа с удалённым репозиторием

## Настройка удалённого репозитория
```bash
git remote add origin https://github.com/oleg977/Python-templates.git

Отправк изменений
git push origin main

Отмена последнего комминта
git reset --soft HEAD~1

Получение изменений
git pull origin main

Если ошибка  rejected updates
git pull origin main
git push origin main

Конфликты с удалённым репозиторием
git pull origin main --allow-unrelated-histories
---
### 4. **Работа с ветками**

Создайте файл `branches.md`:

```markdown
# Работа с ветками

## Создание новой ветки
```bash
git branch feature-branch

Переключение на ветку
git checkout feature-branch

Слияние ветток
git checkout main
git merge feature-branch

Удаление ветки
git branch -d feature-branch
Если конфликт, ввести изменения и коммит
git add <file_name>
git commit -m "Resolve merge conflict"
---

### 5. **Игнорирование файлов**

Создайте файл `ignoring_files.md`:

```markdown
# Игнорирование файлов

## Создание `.gitignore`
Создайте файл `.gitignore` в корне проекта и добавьте в него пути к игнорируемым файлам:
