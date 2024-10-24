@echo off
cd C:\Users\harsh\Desktop\Leetcode
echo Starting Git Sync on %date% %time% >> sync_log.txt
git add . >> sync_log.txt 2>&1
git commit -m "Auto-sync on %date% %time%" >> sync_log.txt 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Commit failed, possibly no changes to commit. >> sync_log.txt 2>&1
) else (
    git push origin master >> sync_log.txt 2>&1
)
echo Sync completed on %date% %time% >> sync_log.txt 2>&1
