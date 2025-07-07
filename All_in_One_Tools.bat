@echo off
setlocal enabledelayedexpansion

::======================================================================
:: Admin Check
::======================================================================
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :main_menu
) else (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~s0' -Verb RunAs"
    exit /b
)

:main_menu
powershell -Command "$Host.UI.RawUI.FontSize = 20" >nul 2>&1
cls
color 0a
title All in One Tools

echo  ██╗      ██████╗  ██████╗ ██╗ ██████╗  ██████╗ ███╗   ██╗███████╗███████╗
echo  ██║     ██╔═══██╗██╔════╝ ██║██╔═══██╗██╔═══██╗████╗  ██║██╔════╝██╔════╝
echo  ██║     ██║   ██║██║  ███╗██║██║   ██║██║   ██║██╔██╗ ██║█████╗  ███████╗
echo  ██║     ██║   ██║██║   ██║██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║
echo  ███████╗╚██████╔╝╚██████╔╝██║╚██████╔╝╚██████╔╝██║ ╚████║███████╗███████║
echo  ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝
echo.
echo ======================================================================
echo                        ALL IN ONE TOOLS
echo ======================================================================
echo.
echo   1. Commands Tools
echo   2. Defender Utility
echo   3. System Repair
echo   4. Windows Maintenance Utility
echo.
echo   X. Exit
echo.
echo ======================================================================
echo.

set /p "choice=Enter your choice: "

if /i "%choice%"=="1" goto :commands_tools_menu
if /i "%choice%"=="2" goto :defender_utility_menu
if /i "%choice%"=="3" goto :system_repair_menu
if /i "%choice%"=="4" goto :windows_maintenance_menu
if /i "%choice%"=="X" goto :eof

echo Invalid choice.
pause
goto :main_menu

::======================================================================
:: Commands Tools Menu
::======================================================================
:commands_tools_menu
cls
echo ===================================
echo       SYSTEM UTILITIES
echo ===================================
echo 1.  Windows Setup Script (Chris Titus)
echo 2.  User Accounts
echo 3.  DirectX Diagnostic
echo 4.  Disk Management
echo 5.  System Configuration
echo 6.  System Information
echo 7.  Power Options
echo 8.  Steps Recorder
echo 9.  Windows Version
echo 10. Network Connections
echo 11. Programs and Features
echo 12. Package Manager (Winget)
echo 13. Update All Packages (Winget)
echo 14. Windows Firewall
echo 15. Temporary Files (Explorer)
echo 16. Performance Options
echo.
echo B.  Back to Main Menu
echo X.  Exit
echo.

set /p "choice=Enter your choice: "

if /i "%choice%"=="1" (
    echo Running Windows Setup Script...
    powershell -Command "Start-Process powershell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command iwr -useb https://christitus.com/win | iex' -Verb RunAs"
    pause
) else if /i "%choice%"=="2" (
    start "" control userpasswords2
) else if /i "%choice%"=="3" (
    start "" dxdiag
) else if /i "%choice%"=="4" (
    start "" diskmgmt.msc
) else if /i "%choice%"=="5" (
    start "" msconfig
) else if /i "%choice%"=="6" (
    start "" msinfo32
) else if /i "%choice%"=="7" (
    start "" powercfg.cpl
) else if /i "%choice%"=="8" (
    start "" psr
) else if /i "%choice%"=="9" (
    start "" winver
) else if /i "%choice%"=="10" (
    start "" ncpa.cpl
) else if /i "%choice%"=="11" (
    start "" appwiz.cpl
) else if /i "%choice%"=="12" (
    start "Winget" cmd /k winget
) else if /i "%choice%"=="13" (
    start "Winget Upgrade All" cmd /k winget upgrade --all
) else if /i "%choice%"=="14" (
    start "" firewall.cpl
) else if /i "%choice%"=="15" (
    start "" explorer %temp%
) else if /i "%choice%"=="16" (
    start "" SystemPropertiesPerformance.exe
) else if /i "%choice%"=="B" (
    goto :main_menu
) else if /i "%choice%"=="X" (
    exit /b
) else (
    echo Invalid choice.
    pause
)
goto :commands_tools_menu

::======================================================================
:: Defender Utility Menu
::======================================================================
:defender_utility_menu
cls
echo.
echo  ██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ███████╗██████╗ 
echo  ██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██╔════╝██╔══██╗
echo  ██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║█████╗  ██████╔╝
echo  ██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██╔══╝  ██╔══██╗
echo  ╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝███████╗██║  ██║
echo   ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
echo.
echo                WINDOWS DEFENDER SECURITY HUB
echo  =============================================================
echo.
echo    [1] Update Virus & Spyware Signatures
echo.
echo    [2] Run a Quick Scan
echo.
echo    [3] Run a Full System Scan
echo.
echo    [B] Back to Main Menu
echo    [Q] Quit
echo.
echo  =============================================================
echo.

CHOICE /C 123BQ /N /M "Select an option [1, 2, 3, B, or Q to quit]: "

if errorlevel 5 goto :EOF
if errorlevel 4 goto :main_menu
if errorlevel 3 goto :RunFullScan
if errorlevel 2 goto :RunQuickScan
if errorlevel 1 goto :UpdateSignatures

:UpdateSignatures
cls
echo.
echo  [+] Initializing signature update...
echo  =============================================================
echo.
"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -SignatureUpdate
echo.
echo  =============================================================
echo.
echo  [+] Update process finished.
pause
goto :defender_utility_menu

:RunQuickScan
cls
echo.
echo  [+] Starting Quick Scan. This may take several minutes.
echo  =============================================================
echo.
"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -Scan -ScanType 1
echo.
echo  =============================================================
echo.
echo  [+] Quick Scan finished.
pause
goto :defender_utility_menu

:RunFullScan
cls
echo.
echo  [+] Starting Full System Scan. This can take a very long time.
echo  [+] Please be patient.
echo  =============================================================
echo.
"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -Scan -ScanType 2
echo.
echo  =============================================================
echo.
echo  [+] Full Scan finished.
pause
goto :defender_utility_menu

::======================================================================
:: System Repair Menu
::======================================================================
:system_repair_menu
cls
echo =============================================
echo               SYSTEM REPAIR
echo =============================================
echo Please choose a command to run:
echo.
echo   1. Run System File Checker (sfc /scannow)
echo   2. DISM Check Health
echo   3. DISM Scan Health
echo   4. DISM Restore Health
echo   5. Repair Windows Image (Online)
echo.
echo   B. Back to Main Menu
echo   0. Exit
echo =============================================
echo.

set /p "choice=Enter your choice (0-5 or B): "

if "%choice%"=="1" goto :sfc_scannow
if "%choice%"=="2" goto :dism_check_health
if "%choice%"=="3" goto :dism_scan_health
if "%choice%"=="4" goto :dism_restore_health
if "%choice%"=="5" goto :repair_windows_image
if "%choice%"=="B" goto :main_menu
if "%choice%"=="0" goto :eof

echo Invalid choice. Please press any key to try again.
pause > nul
goto :system_repair_menu

:sfc_scannow
cls
echo Running System File Checker (sfc /scannow)...
echo This may take a while. Please wait.
echo.
sfc /scannow
echo.
echo SFC scan complete.
goto :repair_common_end

:dism_check_health
cls
echo Running DISM Check Health...
echo.
dism /online /cleanup-image /checkhealth
echo.
echo DISM Check Health complete.
goto :repair_common_end

:dism_scan_health
cls
echo Running DISM Scan Health...
echo This may take a while. Please wait.
echo.
dism /online /cleanup-image /scanhealth
echo.
echo DISM Scan Health complete.
goto :repair_common_end

:dism_restore_health
cls
echo Running DISM Restore Health...
echo This may take a while. Please wait.
echo.
dism /online /cleanup-image /restorehealth
echo.
echo DISM Restore Health complete.
goto :repair_common_end

:repair_windows_image
cls
echo Repairing Windows Image (Online)...
echo This may take a while. Please wait.
echo.
DISM.exe /Online /Cleanup-Image /RestoreHealth /Source:C:\RepairSource\Windows /LimitAccess
echo.
echo Windows Image repair complete.
goto :repair_common_end

:repair_common_end
echo.
echo Operation finished. Press any key to return to the menu.
pause > nul
goto :system_repair_menu

::======================================================================
:: Windows Maintenance Menu
::======================================================================
:windows_maintenance_menu
cls
echo =============================================
echo         WINDOWS MAINTENANCE UTILITY
echo =============================================
echo Please choose a command to run:
echo.
echo   1. Clean Temporary Files (del %%temp%%)
echo   2. Reset Windows Store Cache (wsreset)
echo   3. Clear Prefetch Files
echo   4. Schedule Memory Diagnostic (mdsched)
echo.
echo   B. Back to Main Menu
echo   0. Exit
echo =============================================
echo.

set /p "choice=Enter your choice (0-5 or B): "

if "%choice%"=="1" goto :clean_temp
if "%choice%"=="2" goto :reset_store_cache
if "%choice%"=="3" goto :clear_prefetch
if "%choice%"=="4" goto :schedule_memory_diagnostic
if "%choice%"=="B" goto :main_menu
if "%choice%"=="0" goto :eof

echo Invalid choice. Please press any key to try again.
pause > nul
goto :windows_maintenance_menu

:clean_temp
cls
echo Cleaning Temporary Files (del /q/f/s %%temp%%\*)...
echo.
del /q/f/s %temp%\*
rd /s /q %temp% 2>nul && md %temp% >nul
echo.
echo Temporary files cleaned.
goto :maintenance_common_end



:reset_store_cache
cls
echo Resetting Windows Store Cache (wsreset)...
echo A blank Command Prompt window will appear and close automatically.
echo.
wsreset.exe
echo.
echo Windows Store Cache reset initiated.
goto :maintenance_common_end

:clear_prefetch
cls
echo Clearing Prefetch Files (del C:\Windows\Prefetch\* /q /f)...
echo.
del C:\Windows\Prefetch\* /q /f
echo.
echo Prefetch files cleared.
goto :maintenance_common_end

:schedule_memory_diagnostic
cls
echo Scheduling Windows Memory Diagnostic (mdsched)...
echo You will be prompted to restart your computer now or on the next boot.
echo.
mdsched.exe
echo.
echo Windows Memory Diagnostic scheduler opened.
goto :maintenance_common_end

:maintenance_common_end
echo.
echo Operation finished. Press any key to return to the menu.
pause > nul
goto :windows_maintenance_menu

:eof
exit /b
