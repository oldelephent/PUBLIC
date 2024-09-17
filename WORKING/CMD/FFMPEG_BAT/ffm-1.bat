@ECHO OFF
Setlocal EnableDelayedExpansion
set INPUT="C:\Users\Administrator\Desktop\manish_sir_YOUTUBE"
set OUTPUT="C:\Users\Administrator\Desktop\M_ffmpeg"

:: encode video:

for %%a in ("%INPUT%\*.*")  DO ffmpeg -i "%%a"  -c:v libx265 -threads 1 -c:a copy "%output%\%%~na_%%03d.mp4"

