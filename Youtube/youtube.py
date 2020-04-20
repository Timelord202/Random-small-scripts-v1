from pytube import YouTube
from pathlib import Path
from os import makedirs
from parse_captions import captions
from parse_title import title
import os

url = input('URL: ')
yt = YouTube(url)

title = title().parse_title(yt.title)
stream_video = yt.streams.get_highest_resolution()
stream_audio = yt.streams.get_audio_only()
download_path = Path.home()/'Desktop/Youtube Videos'/title

try:
    makedirs(download_path)
    os.chdir(download_path)
except FileExistsError:
    os.chdir(download_path)

try:
    caps = yt.captions['en']
    norm_captions = captions().parse_captions(caps.generate_srt_captions())

    with open('captions.txt', 'w') as file:
        file.write(norm_captions)
except:
    with open('captions.txt', 'w') as file:
        file.write('No english captions')

stream_audio.download(filename='Audio')
stream_video.download(filename='Video')
