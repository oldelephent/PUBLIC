@echo off
setlocal enabledelayedexpansion

:: Initialize the part number
set part=1

:: Process all .mkv files in the current directory
for /f %%i in ('dir /b *.mkv') do (
    set file=%%i
    call :process_video
    set /a part+=1
)

:process_video
:: Apply ffmpeg command to the selected file with dynamic part number
ffmpeg -i "%file%" -vf "drawtext=text='Part !part!':fontfile=C:/trim/atop-font/Atop-R99O3.ttf:fontcolor=yellow:fontsize=40:x=w-10-text_w:y=h-10:text_h" -codec:a copy "temp_file.mkv"

:: Overwrite the original file with the processed video
move /Y "temp_file.mkv" "%file%"
goto :eof

:end
pause



REM ffmpeg -i %file% -vf "drawtext=text='Part 2':fontfile=C:/trim/atop-font/Atop-R99O3.ttf:fontcolor=yellow:fontsize=40:x=w-10-text_w:y=h-10-text_h" -codec:a copy %file%.mp4
