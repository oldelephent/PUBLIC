

$date_to_parse = Get-Content "E:\date.txt"

$Dir_to_scan = "E:\wav"

foreach ($date in $date_to_parse){

    New-Item -Path $Dir_to_scan\$date -ItemType Directory
    Get-ChildItem -Path $Dir_to_scan | Where-Object { $_.LastWriteTime.Date -eq (Get-Date "$date").Date } | Copy-Item -Destination $Dir_to_scan\$date    
}


