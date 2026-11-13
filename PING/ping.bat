@echo off
title ping


:loop
for /f "tokens=*" %%A in ('ping 127.0.0.1 -n 1 ^| find "TTL="') do (
    echo %date% %time% %%A
    timeout /t 1 /nobreak > nul
)
goto loop









