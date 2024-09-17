@ECHO OFF
Setlocal EnableDelayedExpansion
set INPUT="C:\Users\Administrator\Desktop\manish_sir_YOUTUBE"
set OUTPUT="C:\Users\Administrator\Desktop\M_ffmpeg"

:: encode video:

for %%a in ("%INPUT%\*.*")  DO ffmpeg -i "%%a"  -c:v libx265 -filter:v fps=30 -threads 2 -c:a copy "%output%\%%~na_%%03d.mp4"

