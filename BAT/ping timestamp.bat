@echo off

REM set/p host= 
set host= 127.0.0.21
ping -t %host%|cmd /q /v /c "(pause&pause)>nul & for /l %%a in () do (set /p "data=" && echo(!date! !time! !data!)&ping -n 2 %host%>nul" >log.txt
