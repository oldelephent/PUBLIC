Get-ChildItem -Path . -Filter "16" | Rename-Item -NewName {$_.Name -replace "16" , "17"} 