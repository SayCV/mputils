@chcp 65001
echo,
echo,=====
echo,SPDX-License-Identifier: (GPL-2.0+ OR MIT):
echo,
echo,!!! THIS IS NOT GUARANTEED TO WORK !!!
echo,
echo,Copyright (c) 2018-2020, SayCV
echo,=====
echo,
@echo off&SetLocal EnableDelayedExpansion

:: =====

set "SCRIPT_RUNSTAMP_DATE=%date:~3,4%-%date:~8,2%-%date:~11,2%"
set "SCRIPT_RUNSTAMP_TIME=%time:~0,2%:%time:~3,2%:%time:~6,2%"
set "__DT__=%SCRIPT_RUNSTAMP_DATE% %SCRIPT_RUNSTAMP_TIME%"
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
DELAY 3 >nul 2>&1 || ping -n 3 127.0.0.1>nul
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
