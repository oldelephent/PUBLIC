net stop terservice
ren c:\Windows\System32\termsrv.dll  c:\Windows\System32\termsrv.dll.bak
xcopy %userprofile%\desktop\termsrv.dll c:\Windows\system32\
net start termservice

