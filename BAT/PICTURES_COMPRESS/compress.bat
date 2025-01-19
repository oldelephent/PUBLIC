REM THIS COMPRESS ALL JPG SAVE THEM WITH COMPRESS IN FRONT OF FILE NAME IN SAME DIR
REM for %%a in (*.jpg) do ffmpeg -i "%%a" -q:v 25 "compressed_%%a"

REM THIS COMPRESS ALL JPG AND SAVE THEM WITH COMPRESS IN BACK OF FILE NAME IN SAME DIR
REM for %%a in (*.jpg) do ffmpeg -i "%%a" -q:v 25 "%%~na_compressed.jpg"


REM THIS COMPRESS ALL JPG AND SAVE THEM IN SEPRATE COMP DIR WITH COMPRESSED AT THE END OF THE FILE
REM for %%a in (*.jpg) do ffmpeg -i "%%a" -q:v 25 "comp\%%~na_compressed.jpg"


REM THIS COMPRESS ALL JPG AND SAVE THEM IN SEPRATE COMP DIR 
REM for %%a in (*.jpg) do ffmpeg -i "%%a" -q:v 25 "comp\%%~na.jpg"


REM THIS COMPRESS ALL JPG AND SAVE THEM IN SEPRATE DIR CREATE DIR IF NOT ALREADY THERE
REM mkdir all_compress_images
REM for %%a in (*.jpg) do ffmpeg -i "%%a" -q:v 25 "all_compress_images\%%~na.jpg"


REM SUPPORT TWO FORMAT 
REM for %%a in (*.jpeg *.jpg) do ffmpeg -i "%%a" -q:v 25 "test\%%~na.jpg"

REM COMPRESS ALL FORMAT JPG JPEG PNG KEEP THE NAME AND EXTENSION SAME 
REM for %%a in (*.*) do ffmpeg -i "%%a" -q:v 25 "test\%%~na%%~xa"
