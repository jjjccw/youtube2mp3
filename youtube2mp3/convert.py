import os
import pathlib

from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import confirm
from pytube import YouTube

# get the url from the user
yt = YouTube(
    prompt("> Enter the URL of the video to convert: \n")
)

# extract audio from first result
video = yt.streams.filter(only_audio=True).first()

# save in user home directory
home = pathlib.Path.home()
print(home)


