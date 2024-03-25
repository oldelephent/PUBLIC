@echo off
setlocal enabledelayedexpansion

set "directory=C:\Users\USER\Downloads\REN"

set /p a="enter number"
set /p b="enter number"


for %%F in ("%directory%\*%a%*") do (
    set "filename=%%~nxF"
    ren "%%F" "!filename:%a%=%b%!"
)
