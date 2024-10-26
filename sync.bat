@echo off
setlocal

REM Change to your Leetcode directory
cd C:\Users\harsh\Desktop\Leetcode

REM Log start time
echo Starting Git Sync on %date% %time% >> sync_log.txt

REM Create .gitkeep in every empty folder
for /d %%d in (*) do (
    pushd "%%d"
    if not exist "*" (
        echo. > ".gitkeep"
    )
    popd
)

REM Check for changes and add all files and directories
git add -A >> sync_log.txt 2>&1

REM Commit changes
git commit -m "Auto-sync on %date% %time%" >> sync_log.txt 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Commit failed, possibly no changes to commit. >> sync_log.txt 2>&1
) else (
    REM Push to the main branch
    git push origin master >> sync_log.txt 2>&1
)

REM Log end time
echo Sync completed on %date% %time% >> sync_log.txt 2>&1

endlocal
