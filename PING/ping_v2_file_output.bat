@echo off
setlocal EnableDelayedExpansion

:loop
for /f "tokens=*" %%A in ('ping -4 -n 1 google.com 2^>^&1 ^| findstr /i /c:"TTL=" /c:"timed out" /c:"could not find" /c:"unreachable" /c:"General failure"') do (
    echo !date! !time! %%A
    echo !date! !time! %%A >> "%userprofile%\desktop\ping_data.txt"
)
timeout /t 1 /nobreak >nul
goto loop
