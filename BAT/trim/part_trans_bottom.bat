@ECHO OFF
Setlocal EnableDelayedExpansion
set INPUT="C:\trim\trim"
set OUTPUT="C:\trim\trimm"

:: Initialize part counter
set PART=1

:: Loop through each video file in the input directory
for %%a in ("%INPUT%\*.*") DO (
    :: Encode video with bottom center, semi-transparent part label
    ffmpeg -i "%%a" -vf "drawtext=text='Part !PART!':fontfile=C:/trim/atop-font/Atop-R99O3.ttf:fontcolor=yellow@0.5:fontsize=40:x=(w-text_w)/2:y=h-10-text_h" -codec:a copy "%OUTPUT%\%%~na.mp4"
    
    :: Increment the part counter for the next file
    set /a PART+=1
)

:: End the script
endlocal



REM ffmpeg -i .\Golmaal_Returns.mp4 -map 0:v:0 -map 0:a:0 -f segment -segment_time 600 -c copy -reset_timestamps 1 -segment_start_number 1 .\Golmaal_Returns%02d.mkv (trim video in parts)