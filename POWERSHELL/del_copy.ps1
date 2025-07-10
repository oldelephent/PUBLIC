$base_path = ""

#$copy_source_path = "copy\des - Copy\*" for copy-item

$copy_source_path = "copy\des - Copy\" # for robocopy

Get-ChildItem -Path $base_path  | Where-Object { $_.Name -ne 'c.txt' } | Remove-Item -Force

timeout.exe /T 5

#Copy-Item $copy_source_path -Destination $base_path

Robocopy.exe $copy_source_path  $base_path  *.* /MT:16

$today_date = (Get-Date).ToString('dd-MM-yyy')
#how to get telegram token chat text https://www.youtube.com/watch?v=UhZtrhV7t3U
$token = "123456789:abcd-efghij-klmnop"
$chat = "-987654321"
$text = "Files are copied $today_date"
$data = "https://api.telegram.org/bot$token/sendMessage?chat_id=$chat&text=$text"

Invoke-RestMethod -Uri $data -Method Post -ContentType "application/json" -Body (@{
    chat_id = $chat
    text = $text
} | ConvertTo-Json -Depth 3)

