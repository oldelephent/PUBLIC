Get-Content "ip.txt" | ForEach-Object {ping -n 1 -a $_ | Select-Object -First 2} >> hostname.txt