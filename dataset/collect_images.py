import cv2 as cv
import os
import yt_dlp
import sys
import time
dataset = sys.argv[1]

images = []
videos = {}
file = sys.argv[1]

folder_name = file.split('.')[0]
print(folder_name)
with open(file, 'r') as f:
    for line in f:
        images.append(line.strip())

if not os.path.exists(folder_name) : os.makedirs(folder_name)
if not os.path.exists('videos') : os.makedirs('videos')

processed_videos = []
files = os.listdir(folder_name)
for file in files:
    file = file.split('#')[0]
    processed_videos.append(file)
processed_videos = set(processed_videos)
print(len(processed_videos))
for image in images:
    image = image.split('#')
    id_video = image[0]
    id_frame = image[1].split('.')[0]
    if id_video not in videos:
        videos[id_video] = []
    videos[id_video].append(id_frame)

for filename, frames in videos.items():
    link = "https://www.youtube.com/watch?v=" + filename
    if filename + '.mp4' in os.listdir('videos') or filename in processed_videos:
        continue
    retry_attempts = 3  # Maximum number of retry attempts
    for attempt in range(retry_attempts):
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'videos/%(id)s.%(ext)s',
                'referer': link,
                'no-check-certificate': True,
                'cookies-from-browser': 'chrome',
                'add-header': 'Accept:*/*'
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            break  # Download successful, exit the retry loop
        except Exception as e:
            print(f"Download error for {link}. Retrying ({attempt+1}/{retry_attempts})...")
            time.sleep(5)  # Wait for 5 seconds before retrying

    video = cv.VideoCapture("videos/" + filename + ".mp4")
    for frame in frames:
        video.set(cv.CAP_PROP_POS_FRAMES, float(frame))
        res, image = video.read()
        if res:
            image_filename = f"{folder_name}/{filename}#{frame}.jpg"
            cv.imwrite(image_filename, image)
            print(f"Saved image: {image_filename}")
    os.remove("videos/" + filename + ".mp4")
