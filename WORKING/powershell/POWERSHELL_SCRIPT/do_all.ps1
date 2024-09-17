Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections" -value 0
#Enable RDP

Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name UserAuthentication 0
#Set Disable NLA

Set-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Lsa -Name LimitBlankPasswordUse 0
#Enable to set no password