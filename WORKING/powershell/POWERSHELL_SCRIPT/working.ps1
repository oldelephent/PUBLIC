if((Get-Process -Name notepad -ErrorAction SilentlyContinue) -eq $null){
    ."C:\Windows\notepad.exe"
}


