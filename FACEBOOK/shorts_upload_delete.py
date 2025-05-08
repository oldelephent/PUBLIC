import os
import requests
import json
import time

# Facebook access token

with open('key.txt','r') as f1:
    key = f1.read()

access_token = key
channel_id = "123456789"

#hashtag = "#anime #manga #art #otaku #animeart #animegirl #cosplay #animeedits #naruto #fanart #drawing #kawaii #animememes #animeedit #onepiece #memes #animelover #digitalart #cute #artist #love #animes #meme #japan #dragonball #weeb #animegirls #cosplayer #animefan #artwork"

# URL of the Facebook Graph API endpoint
url_start = f"https://graph.facebook.com/v22.0/{channel_id}/video_reels"

# Headers for the requests
headers = {
    "Content-Type": "application/json"
}

# Folder where videos are stored
folder_path = r'C:\folder'
video_files = os.listdir(folder_path)

# Loop through all the video files
for video_file in video_files:
    video_path = os.path.join(folder_path, video_file)

    # Step 1: Start the upload phase for each video file
    data = {
        "upload_phase": "start",
        "access_token": access_token
    }

    print(f"Starting upload session for {video_file}...")

    response = requests.post(url_start, headers=headers, data=json.dumps(data))
    response_json = response.json()

    # Extract the video_id from the response
    video_id = response_json.get("video_id")
    if not video_id:
        print(f"Error starting video upload for {video_file}: {response_json}")
        continue

    print(f"Upload session started for {video_file}, video_id: {video_id}")

    # Step 2: Upload video content (file size may vary, make sure to adjust accordingly)
    url_upload = f"https://rupload.facebook.com/video-upload/v22.0/{video_id}"
    file_size = os.path.getsize(video_path)  # Get the size of the video file
    headers_upload = {
        "Authorization": f"OAuth {access_token}",
        "offset": "0",
        "file_size": str(file_size)
    }

    # Open the file and upload
    with open(video_path, "rb") as file:
        upload_response = requests.post(url_upload, headers=headers_upload, data=file)

    if upload_response.status_code != 200:
        print(f"Error uploading video {video_file}: {upload_response.text}")
        continue

    print(f"Successfully uploaded video {video_file}, video_id: {video_id}")

    # Step 3: Finish the upload and publish the video
    url_finish = f"https://graph.facebook.com/v22.0/{channel_id}/video_reels"
    params = {
        'access_token': access_token,
        'video_id': video_id,
        'upload_phase': 'finish',
        'video_state': 'PUBLISHED',
        'description': video_file + '\n\n\n' #+ hashtag  # Optional: use a description like the file name
    }

    finish_response = requests.post(url_finish, params=params)

    if finish_response.status_code == 200:
        print(f"Successfully finished and published video {video_file}")
        # Delete the video file from the local system after posting
        os.remove(video_path)
        print(f"Deleted local video file {video_file}")
    else:
        print(f"Error finishing video upload {video_file}: {finish_response.text}")

    # Add a small delay to avoid rate-limiting issues (optional)
    time.sleep(2)

print("All videos have been processed.")


