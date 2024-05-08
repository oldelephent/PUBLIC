Get-ChildItem -Path . -Filter *22* | Rename-Item -NewName {$_.Name -replace "22" , "23"} 

#ls -Filter *22* | measure
ls -Filter *23* | measure