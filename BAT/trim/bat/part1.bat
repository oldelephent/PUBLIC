@ECHO OFF
Setlocal EnableDelayedExpansion
set INPUT="C:\trim\trim"
set OUTPUT="C:\trim\trimm"

:: encode video:

for %%a in ("%INPUT%\*.*")  DO ffmpeg -i "%%a" -vf "drawtext=text='Part 1':fontfile=C:/trim/atop-font/Atop-R99O3.ttf:fontcolor=yellow:fontsize=40:x=w-10-text_w:y=h-10-text_h" -codec:a copy "%output%\%%~na_%%03d.mp4"


REM for %%a in ("%INPUT%\*.*")  DO ffmpeg -i "%%a"  -c:v libx265 -filter:v fps=30 -threads 2 -c:a copy "%output%\%%~na_%%03d.mp4"
REM ffmpeg -i %file% -vf "drawtext=text='Part 2':fontfile=C:/trim/atop-font/Atop-R99O3.ttf:fontcolor=yellow:fontsize=40:x=w-10-text_w:y=h-10-text_h" -codec:a copy %file%.mp4
