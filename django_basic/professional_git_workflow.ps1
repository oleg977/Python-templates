# Установка oh-my-posh
# winget install JanDeDobbeleer.OhMyPosh -s winget

# Или через PowerShell Gallery:
# Install-Module oh-my-posh -Scope CurrentUser

# Проверьте наличие Git
# Get-ChildItem "C:\Program Files\Git\bin\git.exe" -ErrorAction SilentlyContinue
# Get-ChildItem "C:\Program Files (x86)\Git\bin\git.exe" -ErrorAction SilentlyContinue

# Настройка Git в PyCharm
# File  > Setting  > Version Control > Git
# C:\Program Files\Git\bin\git.exe

# Проверить где находтся Git
# Проверьте наличие Git
# Get-ChildItem "C:\Program Files\Git\bin\git.exe" -ErrorAction SilentlyContinue
# Get-ChildItem "C:\Program Files (x86)\Git\bin\git.exe" -ErrorAction SilentlyContinue

# Создайте или отредактируйте профиль PowerShell:
# Откройте профиль для редактирования
# notepad $PROFILE
# Если файла нет, создайте его:
# New-Item -Path $PROFILE -Type File -Force

# Добавляем Git в PATH
# $env:PATH += ";C:\Program Files\Git\bin"
# Добавьте в ваш $PROFILE эту функцию:
function
global:prompt
{
# Базовый путь
$path = $(Get - Location)

# Получаем информацию о Git репозитории
$gitBranch = ""
$gitStatus = git
status - -porcelain
2 >$null
$branch = git
rev - parse - -abbrev - ref
HEAD
2 >$null

if ($branch)
{
$gitBranch = " [$branch]"
}

# Цвета
Write - Host
"PS $path" - NoNewline - ForegroundColor
Green
Write - Host $gitBranch - NoNewline - ForegroundColor
Yellow
Write - Host
"> " - NoNewline - ForegroundColor
White

return " "
}
# Установите oh-my-posh для профессионального prompt:
# Добавьте в $PROFILE:
# Добавляем Git в PATH
$env:PATH += ";C:\Program Files\Git\bin"

# Инициализируем oh-my-posh
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\atomic.omp.json" | Invoke-Expression

# После редактирования $PROFILE:# Перезагрузите профиль
# . $PROFILE
#
# # Или просто откройте новое окно PowerShell

# Сначала найдем где находится ваш $PROFILE:
# Откройте его и добавьте ОБА решения:
# Добавляем Git в PATH постоянно
$env: PATH += ";C:\Program Files\Git\bin"

# Функция для красивого prompt с Git веткой
function
global:prompt
{
$path = $(Get - Location)
$gitBranch = ""

# Проверяем Git репозиторий
$branch = git
rev - parse - -abbrev - ref
HEAD
2 >$null
if ($branch) {
$gitBranch = " [$branch]"
}

Write - Host
"PS $path" - NoNewline - ForegroundColor
Green
Write - Host $gitBranch - NoNewline - ForegroundColor
Yellow
Write - Host
"> " - NoNewline - ForegroundColor
White
return " "
}
# Это более надежный способ:
# Установите oh-my-posh
winget install JanDeDobbeleer.OhMyPosh -s winget

# Или если winget не работает:
Install-Module oh-my-posh -Scope CurrentUser -Force

# Затем в $PROFILE добавьте:

3. Постоянное решение для PATH
Добавьте Git в системный PATH через переменные окружения:

Нажмите Win + R, введите sysdm.cpl
Дополнительно → Переменные среды
В Системные переменны найдите Path
Изменить → Создать
Добавьте: C:\Program Files\Git\bin
Нажмите OK

# Проверьте в каждом проекте:
# В проблемном проекте проверьте:
git status
git rev-parse --abbrev-ref HEAD

# Убедитесь что это Git репозиторий:
Get-ChildItem -Hidden -Force | Where-Object Name -eq ".git"

# Решение для проекта без Git
# Перейдите в папку проекта
cd C:\Users\Anack\fkask_basic

# Инициализируйте Git
git init

# Добавьте удаленный репозиторий (если нужно)
git remote add origin URL_ВАШЕГО_РЕПОЗИТОРИЯ

# Сделайте первый коммит
git add .
git commit -m "Initial commit"

# Обновите вашу функцию в $PROFILE, чтобы она корректно обрабатывала не-Git папки:
function
global:prompt
{
$path = $(Get - Location)
$gitBranch = ""

# Проверяем находится ли мы в Git репозитории
$isGitRepo = git
rev - parse - - is -inside - work - tree
2 >$null
if ($isGitRepo -eq "true") {
$branch = git rev-parse --abbrev-ref HEAD 2 > $null
if ($branch) {
$gitBranch = " [$branch]"
}
}

Write - Host
"PS $path" - NoNewline - ForegroundColor
Green
Write - Host $gitBranch - NoNewline - ForegroundColor
Yellow
Write - Host
"> " - NoNewline - ForegroundColor
White
return " "
}
# Убедитесь, что вы в правильной папке:
# Посмотрите что в папке
Get-ChildItem

# Или найдите .git папку в родительских директориях
Get-ChildItem -Hidden -Force -Recurse -Depth 3 | Where-Object Name -eq ".git"

# 1. Проверьте текущую функцию prompt
# Посмотрите какая функция prompt сейчас активна
Get-Content function:\prompt

# Добавьте в ваш $PROFILE исправленную версию:
function
global:prompt
{
$path = $(Get - Location)
$gitBranch = ""

# Безопасная проверка Git репозитория
try {
$branch = git rev-parse --abbrev-ref HEAD 2 > $null
if ($branch - and $branch -ne "HEAD") {
$gitBranch = " [$branch]"
}
} catch {
# Игнорируем ошибки, если это не Git репозиторий
}

Write - Host
"PS $path" - NoNewline - ForegroundColor
Green
Write - Host $gitBranch - NoNewline - ForegroundColor
Yellow
Write - Host
"> " - NoNewline - ForegroundColor
White
return " "
}
# 3. Примените изменения
# Перезагрузите профиль
. $PROFILE

# Или закройте и откройте новое окно PowerShell/PyCharm
4. Проверьте в проекте shoplist
cd C:\Users\Anack\Documents\GitHub\shoplist
# Должно показать: PS C:\Users\Anack\Documents\GitHub\shoplist [main]>

# Если ничего не помогает, удалите и заново создайте функцию:
# Удалите текущую функцию
Remove-Item function:\prompt
# Добавьте заново из профиля
. $PROFILE
Обновите функцию в $PROFILE:
function
global:prompt
{
$path = $(Get - Location)
$gitBranch = ""
$venv = ""

# Проверяем виртуальное окружение
if ($env:VIRTUAL_ENV) {
$venvName = Split-Path $env:VIRTUAL_ENV - Leaf
$venv = " ($venvName)"
}

# Проверяем Git репозиторий
try {
$branch = git rev-parse --abbrev-ref HEAD 2 > $null
if ($branch - and $branch -ne "HEAD") {
$gitBranch = " [$branch]"
}
} catch {
# Игнорируем ошибки
}

Write - Host
"PS $path" - NoNewline - ForegroundColor
Green
Write - Host $gitBranch - NoNewline - ForegroundColor
Yellow
Write - Host $venv - NoNewline - ForegroundColor
Cyan
Write - Host
"> " - NoNewline - ForegroundColor
White
return " "
}
# Запускать
.\professional_git_workflow.ps1