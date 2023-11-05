@echo off
setlocal enabledelayedexpansion
:: Set the common password
set common_password=123

:: Number of users to create
set /p n="enter number of user"

:: Loop to create users
for /l %%i in (1, 1, %n%) do (
    set username=pc%%i
    
    :: Create the user account with the same password
    net user !username! %common_password% /add
)

REM :: Pause to keep the command prompt window open
REM pause
