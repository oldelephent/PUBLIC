#powershell.exe -NoLogo -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File "C:\run.ps1"

while ($true) {if ((Get-Service spooler).Status -eq 'Stopped') { Start-Service spooler } start-sleep 5}


