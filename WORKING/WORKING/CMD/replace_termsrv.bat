net stop termservice
takeown /F c:\Windows\System32\termsrv.dll /A
timeout /T 5
icacls c:\Windows\System32\termsrv.dll /grant administrators:F
timeout /T 5
xcopy %userprofile%\desktop\termsrv.dll system32\
net start termservice 


