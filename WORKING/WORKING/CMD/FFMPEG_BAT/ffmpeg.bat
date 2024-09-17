Set INPUT="E:\ABHISHEK\MOVIES_SHOWS\WATCHING"

Set OUTPUT="E:\ABHISHEK\MOVIES_SHOWS\W"

for %%a in ("%INPUT%\*.*") DO ffmpeg.exe -i "%%a" -c:v libx265 -filter:v fps=60 -threads 14 -c:a copy "%OUTPUT%/%%~na.mp4"



