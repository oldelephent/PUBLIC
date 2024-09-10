    

$ltd = (Get-Date).AddDays(-1).ToString('ddMMyyyy')
$current = (Get-Date).ToString('ddMMyyyy')

(Get-Date).ToString('ddMMyyyy')




Get-ChildItem -Path e:\ren -Filter *$ltd* -Verbose | Rename-Item -NewName {$_.Name -replace "$ltd" , "$C1" } -Verbose
Get-ChildItem -Path e:\ren -Filter *$d2* -Verbose | Rename-Item -NewName {$_.Name -replace "$d2" , "$c2" } -Verbose
Get-ChildItem -Path e:\ren -Filter *$d3* -Verbose | Rename-Item -NewName {$_.Name -replace "$d3" , "$c3" } -Verbose

