
start cmd.exe /K cd "C:\Users\ABHISHEK\Documents\WORKING\CMD\REN" for /f %%a in ('type "C:\Users\ABHISHEK\Documents\WORKING\CMD\curlist.txt"') do curl -O %%a 



REM start cmd.exe /K "C:\Users\ABHISHEK\Documents\WORKING\CMD\REN" "curl.exe -O "C:\Users\ABHISHEK\Documents\WORKING\CMD\curlist.txt""