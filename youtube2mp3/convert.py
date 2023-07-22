import os
import pathlib
import subprocess

from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import confirm
from pytube import YouTube

from moviepy.editor import VideoFileClip

# get the url from the user
yt = YouTube(
    prompt("> Enter the URL of the video to convert: ")
)

# extract audio from first result
video = yt.streams.filter(only_audio=True).first()
title = yt.title

# Find user's home directory and create youtube2mp3 directory
# in Downloads, e.g. ~/Downloads/youtube2mp=3
# this is where we put all final .mp3 files
home = pathlib.Path.home()
path = pathlib.Path(f"{home}/Downloads/youtube2mp3")
path.mkdir(parents=True, exist_ok=True)

print("path before:\n")
subprocess.run(["ls", path])

# download the file
video_raw = video.download(output_path=path, filename=f"{title}.mp4")

# save the file
# base, ext = os.path.splitext(video_raw)
# video_mp3 = base + '.mp3'
# os.rename(video_raw, video_mp3)

print("path after:\n")
subprocess.run(["ls", path])

print("name and type before: ")
subprocess.run(["ls", path])
subprocess.run(["file", f"{path}/metal pipe falling sound effect.mp4"])

moviepy_video = VideoFileClip(os.path.join(f"{path}/{title}.mp4"))
moviepy_video.audio.write_audiofile(os.path.join(f"{path}/{title}.mp3"))

print("name and type after: ")
subprocess.run(["ls", path])
subprocess.run(["file", f"{path}/metal pipe falling sound effect.mp3"])




