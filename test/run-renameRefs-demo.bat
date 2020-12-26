@chcp 65001
@echo off
echo,
echo,=====
echo,SPDX-License-Identifier: (GPL-2.0+ OR MIT):
echo,
echo,!!! THIS IS NOT GUARANTEED TO WORK !!!
echo,
echo,Copyright (c) 2018-2020, SayCV
echo,=====
echo,
@echo off&setLocal EnableDelayedExpansion

if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

setlocal disabledelayedexpansion
set GanTanHaoMark=!
setlocal enabledelayedexpansion

:: =====
cd /d "%~dp0"
set "TOPDIR=%cd:\=/%"
title "%~n0"
:: =====

if "xy" == "xy" goto :skip_getadmin_privileges
>NUL 2>&1 REG.exe query "HKU\S-1-5-19" || (
    ECHO SET UAC = CreateObject^("Shell.Application"^) > "%TEMP%\Getadmin.vbs"
    ECHO UAC.ShellExecute "%~f0", "%1", "", "runas", 1 >> "%TEMP%\Getadmin.vbs"
    "%TEMP%\Getadmin.vbs"
    DEL /f /q "%TEMP%\Getadmin.vbs" 2>NUL
    Exit /b
)
:skip_getadmin_privileges

set "SCRIPT_RUNSTAMP_DATE=%date:~3,4%-%date:~8,2%-%date:~11,2%"
set "SCRIPT_RUNSTAMP_TIME=%time:~0,2%:%time:~3,2%:%time:~6,2%"
set "__DT__=%SCRIPT_RUNSTAMP_DATE% %SCRIPT_RUNSTAMP_TIME%"
set "VER=1.0.5-20201226"
echo %__DT__% [INFO] Check script version : %VER%.
echo %__DT__% [INFO] Running %~n0.

:: =====
call :checkProgramExist powerlogic
call :checkProgramExist python

:: ====================================================================================================
:: ----------------------------------------------------------------------------------------------------

call python padssch_rename_refs.py

:: ----------------------------------------------------------------------------------------------------
:: ====================================================================================================

if not %errorlevel% == 0 echo %__DT__% [INFO] Running failed && pause && EXIT 1
echo %__DT__% [INFO] Running successfully

:: =====
DELAY 3 2>nul || ping -n 3 127.0.0.1>nul
EXIT 0

:: =====
:: =====

:: Check the program if exist
:checkProgramExist
    set "cmd=which %~1"

    for /f "delims=" %%a in ('!cmd! 2^>nul') do (
        set "line=%%a"
        echo %__DT__% [INFO] Try to found %~1 : !line!
        EXIT /B 0
    )
    echo %__DT__% [INFO] Try to found %~1 : failed
    EXIT /B 0
