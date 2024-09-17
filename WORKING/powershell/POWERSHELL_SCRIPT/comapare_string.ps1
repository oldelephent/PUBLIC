$string1 = Read-Host "enter your string"
$string2 = Read-Host "enter your string"

if($string1.Length -eq $string2.Length )
{Write-Host "$string1 equal"}

elseif ($string1.Length -gt $string2.Length) {
    Write-Host "$string1 it's greater"
}
elseif ($string1.Length -le $string2.Length) {
    Write-Host "$string1 it's small"        

}





