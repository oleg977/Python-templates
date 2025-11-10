<#
.SYNOPSIS
    Professional Git Workflow Setup for Team Development
#>

function Show-Header {
    Write-Host "`n"
    Write-Host "🚀 PROFESSIONAL GIT WORKFLOW SETUP" -ForegroundColor Cyan
    Write-Host "==========================================" -ForegroundColor Cyan
    try {
        $gitVersion = git --version 2>$null
        if ($gitVersion) {
            Write-Host "Git Version: $gitVersion" -ForegroundColor White
        }
    } catch {
        Write-Host "Git: Not available" -ForegroundColor Red
    }
    Write-Host "Working Dir: $(Get-Location)" -ForegroundColor Gray
}

function Test-GitRepository {
    if (-not (Test-Path ".git")) {
        Write-Host "❌ ERROR: Not a Git repository!" -ForegroundColor Red
        Write-Host "💡 SOLUTION: Run 'git init' first" -ForegroundColor Yellow
        return $false
    }
    return $true
}

function Test-RemoteConnection {
    $remote = git remote get-url origin 2>$null
    if ($remote) {
        Write-Host "✓ Connected to remote: $remote" -ForegroundColor Green
        return $true
    } else {
        Write-Host "⚠ WARNING: No remote repository configured" -ForegroundColor Yellow
        Write-Host "   Run: git remote add origin <your-repo-url>" -ForegroundColor White
        return $false
    }
}

function Show-Status {
    Write-Host "`n📊 CURRENT REPOSITORY STATUS:" -ForegroundColor Yellow
    Write-Host "──────────────────────────────────────" -ForegroundColor Yellow

    # Current branch
    $branch = git branch --show-current 2>$null
    if ($branch) {
        Write-Host "📍 Current branch: $branch" -ForegroundColor White
    }

    # Status
    $status = git status --short 2>$null
    if ($status) {
        Write-Host "`nChanges:" -ForegroundColor Gray
        $status
    } else {
        Write-Host "✓ Working directory clean" -ForegroundColor Green
    }
}

function Show-GitCommands {
    Write-Host "`n🔧 ESSENTIAL GIT COMMANDS:" -ForegroundColor Green
    Write-Host "──────────────────────────────────────" -ForegroundColor Green

    Write-Host "`n📁 BASIC WORKFLOW:" -ForegroundColor Yellow
    Write-Host "  git status                          # Check status" -ForegroundColor White
    Write-Host "  git add .                           # Stage all changes" -ForegroundColor White
    Write-Host "  git commit -m 'descriptive message' # Commit changes" -ForegroundColor White
    Write-Host "  git push origin main               # Push to remote" -ForegroundColor White
    Write-Host "  git pull origin main               # Pull updates" -ForegroundColor White

    Write-Host "`n🌿 BRANCHING STRATEGY:" -ForegroundColor Yellow
    Write-Host "  git branch                          # List branches" -ForegroundColor White
    Write-Host "  git checkout -b feature/name       # Create feature branch" -ForegroundColor White
    Write-Host "  git checkout main                  # Switch to main" -ForegroundColor White
    Write-Host "  git merge feature/name             # Merge feature" -ForegroundColor White
    Write-Host "  git branch -d feature/name         # Delete branch" -ForegroundColor White

    Write-Host "`n🔄 ADVANCED WORKFLOW:" -ForegroundColor Yellow
    Write-Host "  git log --oneline --graph          # Visual history" -ForegroundColor White
    Write-Host "  git diff                           # Show changes" -ForegroundColor White
    Write-Host "  git stash                          # Temporary save" -ForegroundColor White
}

function Show-Aliases {
    Write-Host "`n⚡ PRODUCTIVITY ALIASES:" -ForegroundColor Magenta
    Write-Host "──────────────────────────────────────" -ForegroundColor Magenta

    Write-Host "gs   = git status" -ForegroundColor White
    Write-Host "ga   = git add ." -ForegroundColor White
    Write-Host "gc   = git commit -m 'message'" -ForegroundColor White
    Write-Host "gp   = git push" -ForegroundColor White
    Write-Host "gpl  = git pull" -ForegroundColor White
    Write-Host "gl   = git log --oneline --graph" -ForegroundColor White
}

function Show-BestPractices {
    Write-Host "`n🎯 PROFESSIONAL BEST PRACTICES:" -ForegroundColor Cyan
    Write-Host "──────────────────────────────────────" -ForegroundColor Cyan

    Write-Host "✓ Commit small, logical changes" -ForegroundColor Green
    Write-Host "✓ Write descriptive commit messages" -ForegroundColor Green
    Write-Host "✓ Pull before you push" -ForegroundColor Green
    Write-Host "✓ Use feature branches for new work" -ForegroundColor Green
    Write-Host "✓ Review code before merging" -ForegroundColor Green
    Write-Host "✓ Keep main branch always deployable" -ForegroundColor Green
}

# MAIN EXECUTION
try {
    Show-Header

    if (Test-GitRepository) {
        Show-Status
        Test-RemoteConnection
        Show-GitCommands
        Show-Aliases
        Show-BestPractices
    }
}
catch {
    Write-Host "❌ Script execution failed: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`n🎉 Git workflow helper completed!" -ForegroundColor Magenta
