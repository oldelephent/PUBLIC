@ECHO OFF
Setlocal EnableDelayedExpansion

Set INPUT="E:\ABHISHEK\MOVIES_SHOWS\WATCHING"

Set OUTPUT="E:\ABHISHEK\MOVIES_SHOWS\W"

for %%a in ("%INPUT%\*.*")  DO "E:\ABHISHEK\INSTALLED_APPLICATION\ffmpeg\bin\ffmpeg.exe" -i "%%a"  -c:v libx265 -filter:v fps=60 -threads 10 -c:a copy "%output%\%%~na_%%03d.mp4"




