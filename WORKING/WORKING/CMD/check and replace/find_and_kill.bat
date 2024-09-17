@echo off

for /f %%a in ('tasklist ^| find /I "powershell"') do taskkill /F /IM  %%a
