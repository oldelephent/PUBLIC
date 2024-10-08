Get-ItemProperty hklm:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters -Name AllowInsecureGuestAuth 

#change item property
Set-ItemProperty hklm:\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters -Name AllowInsecureGuestAuth -Value 0
