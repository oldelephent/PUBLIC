@ECHO OFF
Setlocal EnableDelayedExpansion
set INPUT="C:\trim\trim"
set OUTPUT="C:\trim\trimm"

:: Initialize part counter
set PART=1

:: Loop through each video file in the input directory
for %%a in ("%INPUT%\*.*") DO (
    :: Encode video with part label
    ffmpeg -i "%%a" -vf "drawtext=text='Part !PART!':fontfile=C:/trim/atop-font/Atop-R99O3.ttf:fontcolor=yellow:fontsize=40:x=w-10-text_w:y=h-10-text_h" -codec:a copy "%OUTPUT%\%%~na.mp4"
    
    :: Increment the part counter for the next file
    set /a PART+=1
)

:: End the script
endlocal
