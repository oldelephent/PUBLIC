@echo off
rem Automatically take the movie name from the current directory (assuming one movie file is in the folder)
for %%F in (c:\trim\trim\*.mp4) do set movie_name=%%F

rem Ask for the segment time in seconds
set /p segment_time=Enter the segment time in seconds (e.g., 600): 

rem Extract movie name without extension
for %%F in (%movie_name%) do set movie_base=%%~nF

rem Run ffmpeg command to split the movie
ffmpeg -i "%movie_name%" -map 0:v:0 -map 0:a:0 -f segment -segment_time %segment_time% -c copy -reset_timestamps 1 -segment_start_number 1 "c:\trim\trim\%movie_base%%%03d.mkv"

echo Movie has been split successfully!
pause


REM ffmpeg -i .Golmaal_Returns.mp4 -map 0:v:0 -map 0:a:0 -f segment -segment_time 600 -c copy -reset_timestamps 1 -segment_start_number 1 .\Golmaal_Returns%02d.mkv
