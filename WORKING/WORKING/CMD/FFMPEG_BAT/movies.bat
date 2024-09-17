@ECHO OFF
Setlocal EnableDelayedExpansion
set INPUT="E:\ABHISHEK\MOVIES_SHOWS\MOVIES"
set OUTPUT="E:\ABHISHEK\MOVIES_SHOWS\W"

:: encode video:

for %%a in ("%INPUT%\*.*")  DO ffmpeg -i "%%a"  -c:v libx265 -filter:v fps=60 -threads 15 -c:a copy "%output%\%%~na_%%03d.mp4"

