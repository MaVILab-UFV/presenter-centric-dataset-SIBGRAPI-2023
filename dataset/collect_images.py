import cv2 as cv
import os
import yt_dlp
import sys

dataset = sys.argv[1]

images = []
videos = {}
if sys.argv[1] == '1':
    with open('complete_dataset.txt', 'r') as f:
        for line in f:
            images.append(line.strip())
    folder_name = "complete_dataset"

elif sys.argv[1] == '2':
    with open('single_person_dataset.txt', 'r') as f:
        for line in f:
            images.append(line.strip())
    folder_name = "single_person_dataset"
    
elif sys.argv[1] == '3':
    with open('annotated_single_person_dataset.txt', 'r') as f:
        for line in f:
            images.append(line.strip())
    folder_name = "annotated_single_person_dataset"

if not os.path.exists(folder_name) : os.makedirs(folder_name)
if not os.path.exists('videos') : os.makedirs('videos')

processed_videos = []
files = os.listdir(folder_name)
for file in files:
    file = file.split('#')[0]
    processed_videos.append(file)
processed_videos = set(processed_videos)

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
    ydl_opts = { 'format' : 'best', 'outtmpl': 'videos/%(id)s.%(ext)s','referer': link,  'no-check-certificate': True,  'cookies-from-browser': 'chrome', 'add-header': 'Accept:*/*'}
    #ydl_opts = { 'format' : '22', 'outtmpl': 'videos/%(id)s.%(ext)s'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    video = cv.VideoCapture("videos/" + filename + ".mp4")
    for frame in frames:
        video.set(cv.CAP_PROP_POS_FRAMES, float(frame))
        res, image = video.read()
        if res:
            cv.imwrite(f"{folder_name}/{filename}#{frame}.jpg", image)
    os.remove("videos/" + filename + ".mp4")
