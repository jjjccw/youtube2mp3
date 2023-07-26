import os
import pathlib
from pathlib import Path

from helpers import *
from moviepy.editor import AudioFileClip
from pytube import YouTube
from pytube import extract
from pytube.cli import on_progress
from pytube.exceptions import AgeRestrictedError


class Youtube2Mp3:
    def __init__(self):
        self.url: str = ""
        self.video: YouTube = None
        self.title: str = ""
        self.save_directory: Path


    def get_youtube_video(self):
        """Takes a URL input from the user to construct a YouTube object

        Returns:
            YouTube: a YouTube video object
        """

        # get the url from the user to create YouTube object
        while True:
            try:
                self.url = yt2mp3_prompt("Enter the URL of the video to convert: ")
                self.video = YouTube(self.url)
                self.video.bypass_age_gate()
                self.video.register_on_progress_callback(on_progress)
                self.title = self.video.title
                break
            except Exception as e:
                print(f"yt2mp3 -- [ERROR] occured when retrieving URL: {e}")
                continue
            
        # confirm this is the right video to convert
        while True:
            choice = yt2mp3_confirm(f"{self.title} was found. Is this the right video to convert")
            if choice:
                self.convert_to_mp3()
                break
            else:
                self.get_youtube_video()
            

    def convert_to_mp3(self):
        # Find user's home directory and create youtube2mp3 directory
        # in ~/Music/youtube2mp3/ , downloaded mp3 files are saved here
        home = pathlib.Path.home()
        path = pathlib.Path(f"{home}/Downloads/youtube2mp3")
        path.mkdir(parents=True, exist_ok=True)
        
        
        # extract audio stream from the top result youtube video
        # and download to youtube2mp3/ as an mp4 initially
        print(self.video)
        audio_stream = self.video.streams\
            .filter(only_audio=True)\
            .first()\
            .download(output_path=path, filename=f"{self.title}.mp4")
        
        if pathlib.Path.exists(Path(f"{path}/{self.title}.mp4")):
            print("yt2mp3  - Video successfully downloaded")

        # # write final audio file as an mp3
        # moviepy_audio = AudioFileClip(os.path.join(f"{path}/{self.title}.mp4"))
        # moviepy_audio.write_audiofile(os.path.join(f"{path}/{self.title}.mp3"))
