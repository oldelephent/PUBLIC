set input=E:\ABHISHEK\MOVIES_SHOWS\WATCHING
set output=E:\ABHISHEK\MOVIES_SHOWS\W


for %%i in %input%\*.*; DO ffmpeg.exe -i %%i -c:v libx265 -filter:v fps:60 -c:a copy "%output%.mp4" 

pause