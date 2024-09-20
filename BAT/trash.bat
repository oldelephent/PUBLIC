for /f %%a in ('type "C:\Users\a\Desktop\list.txt"') do (
    for /r "c:\Windows\System32" %%b in (%%a) do (
        copy "%%b" "%userprofile%\desktop\copy"
    )
)

WORKING
@echo off
for /f %%a in ('type "C:\Users\a\Desktop\list.txt"') do (
    for /r "c:\Windows\System32\" %%b in (*.txt) do (
        copy "%%b" "%userprofile%\desktop\copy"
    )
)




for /f %%a in ('type "C:\Users\a\Desktop\list.txt"') do copy "c:\Windows\System32\%%a" "%userprofile%\desktop\copy"

REM for /f %%a in ('type list.txt') do "robocopy /S c:\Windows\System32\%%a" "%userprofile%\desktop\copy"

REM for /f %%a in ('DIR /s c:\Windows\System32\*txt ^|type list.txt') do copy %%a %userprofile%\desktop\copy
