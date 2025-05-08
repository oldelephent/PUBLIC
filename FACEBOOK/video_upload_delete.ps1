
$key = Get-Content "C:\trim\SHORTS\key.txt"

$accessToken = "$key"
$folderPath = "C:\trim\trimm"
$videoFiles = Get-ChildItem $folderPath -Filter *.mp4
$hashtag = "#anime #manga #art #otaku #animeart #animegirl #cosplay #animeedits #naruto #fanart #drawing #kawaii #animememes #animeedit #memes #onepiece #animelover #digitalart #cute #artist #love #animes #meme #japan #weeb #animegirls #dragonball #cosplayer #animefan #artwork"

# Start the upload process
Write-Host "Starting the video upload process..."

foreach ($video in $videoFiles) {
    $videoFilePath = $video.FullName
    $videoTitle = $video.BaseName
    $videoDescription = $videoTitle + "`n" + $hashtag

    Write-Host "Uploading video: $videoTitle"

    $response = curl -X POST `
        "https://graph-video.facebook.com/v21.0/123456/videos" `
        -F "access_token=$accessToken" `
        -F "title=$videoTitle" `
        -F "description=$videoDescription" `
        -F "file=@$videoFilePath" `
        --limit-rate 3000k

    # Check the response and provide feedback
    if ($response -match '"id":') {
        Write-Host "Successfully uploaded video: $videoTitle"

        # Delete the video after posting
        Write-Host "Deleting video: $videoTitle"
        Remove-Item -Path $videoFilePath
    } else {
        Write-Host "Failed to upload video: $videoTitle. Response: $response"
    }
}

Write-Host "All video uploads have been completed."
