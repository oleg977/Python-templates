# 🚀 Git Practice Guide for Internship

## 📋 Daily Workflow

### Morning Startup
```bash
cd project-folder
git-workflow  # Check status
gpl           # Pull latest changes
```

### Starting New Task
```bash
git-workflow              # Verify clean state
gcb feature/task-name     # Create branch
```

### During Development
```bash
gs                        # Check status
ga                        # Add changes
gc "feat: description"    # Commit
gl                        # View history
```

### Completing Task
```bash
gp                        # Push branch
# Create Pull Request on GitHub
gco main                  # Switch to main
gpl                       # Get updates
```

## 🏋️ Practice Exercises

### Exercise 1: Basic Workflow
```bash
# 1. Create practice branch
gcb practice/basic-workflow

# 2. Create test file
echo "print('Hello Git')" > test.py

# 3. Practice commands
gs
ga  
gc "feat: add test file"
gl
gp

# 4. Cleanup
gco main
git branch -d practice/basic-workflow
```

### Exercise 2: Conflict Resolution
```bash
# 1. Create two branches with same file changes
gcb practice/conflict-branch1
echo "version 1" > conflict.txt
ga && gc "feat: add version 1"

gco main
gcb practice/conflict-branch2  
echo "version 2" > conflict.txt
ga && gc "feat: add version 2"

# 2. Try to merge and resolve
git merge practice/conflict-branch1
# 🔧 Resolve conflict manually
```

## 🎯 Professional Tips

### Commit Messages
- ✅ `feat: add user authentication`
- ✅ `fix: resolve login timeout`
- ❌ `update files`

### Branch Naming
- `feature/user-dashboard`
- `bugfix/login-error`  
- `hotfix/critical-bug`

## 🆘 Quick Help
```bash
git-workflow  # Full status & commands
gs            # Quick status
gl            # History graph
gco branch    # Switch branch
```