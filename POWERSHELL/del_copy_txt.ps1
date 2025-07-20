
$destination_path = ""
$copy_source_path = "" 
$daily_text_file = "c:\"

Get-ChildItem -Path $destination_path | Where-Object { $_.Name -ne 'c.txt' } | Remove-Item -Force

Robocopy.exe $copy_source_path  $destination_path  *.* /MT:16

$today_date = (Get-Date).ToString('dd-MM-yyy')

Get-ChildItem $destination_path | Out-File -FilePath "$daily_text_file\$today_date.txt"

timeout.exe /T 5

#how to get telegram token chat text https://www.youtube.com/watch?v=UhZtrhV7t3U
$token = "fjsadlkfhasdfhasdlkj"
$chat = "-123456789"
$filePath = "$daily_text_file\$today_date.txt"

# Telegram API endpoint
$url = "https://api.telegram.org/bot$token/sendDocument"

# Prepare the form with the document
$form = @{
    chat_id  = $chat
    document = Get-Item -Path $filePath
}

# Send the request
Invoke-RestMethod -Uri $url -Method Post -Form $form
