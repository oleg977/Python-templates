<#
.SYNOPSIS
    Быстрая настройка Git workflow для команды
#>

Write-Host "🚀 БЫСТРАЯ НАСТРОЙКА GIT WORKFLOW" -ForegroundColor Green

# Основные команды Git
Write-Host "`n🔧 ОСНОВНЫЕ КОМАНДЫ:" -ForegroundColor Yellow
Write-Host "git status                          # Проверить статус" -ForegroundColor White
Write-Host "git add .                           # Добавить файлы" -ForegroundColor White
Write-Host "git commit -m 'описание'            # Создать коммит" -ForegroundColor White
Write-Host "git push origin main                # Отправить на GitHub" -ForegroundColor White
Write-Host "git pull origin main                # Получить обновления" -ForegroundColor White

# Работа с ветками
Write-Host "`n🌿 РАБОТА С ВЕТКАМИ:" -ForegroundColor Yellow
Write-Host "git branch                          # Список веток" -ForegroundColor White
Write-Host "git checkout -b new-feature         # Создать ветку" -ForegroundColor White

# Алиасы для быстрой работы
Write-Host "`n⚡ БЫСТРЫЕ АЛИАСЫ:" -ForegroundColor Yellow
Write-Host "function gs { git status }" -ForegroundColor White
Write-Host "function ga { git add . }" -ForegroundColor White
Write-Host "function gc { git commit -m `$args[0] }" -ForegroundColor White
Write-Host "function gp { git push }" -ForegroundColor White

Write-Host "`n🎉 ГОТОВО! Скрипт завершен." -ForegroundColor Magenta

# ОСТАНОВКА СКРИПТА
exit
"@ | Out-File -FilePath "git_workflow_fast.ps1" -Encoding UTF8