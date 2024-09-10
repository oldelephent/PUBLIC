
# Prompt the user for date mappings
$d1 = Read-Host "Enter the old date (e.g., 09092024)"
$c1 = Read-Host "Enter the new date for $d1"
$d2 = Read-Host "Enter the second old date (e.g., 20240910)"
$c2 = Read-Host "Enter the new date for $d2"
$d3 = Read-Host "Enter the third old date (e.g., 10092024)"
$c3 = Read-Host "Enter the new date for $d3"


Get-ChildItem -Path e:\ren -Filter *$d1* -Verbose | Rename-Item -NewName {$_.Name -replace "$d1" , "$C1" } -Verbose
Get-ChildItem -Path e:\ren -Filter *$d2* -Verbose | Rename-Item -NewName {$_.Name -replace "$d2" , "$c2" } -Verbose
Get-ChildItem -Path e:\ren -Filter *$d3* -Verbose | Rename-Item -NewName {$_.Name -replace "$d3" , "$c3" } -Verbose

