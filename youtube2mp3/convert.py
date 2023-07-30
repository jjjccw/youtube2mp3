import os
import pathlib
from pathlib import Path

import pytube
from helpers import *
from moviepy.editor import AudioFileClip
from pytube import YouTube
from pytube import extract
from pytube.cli import on_progress
from pytube.exceptions import AgeRestrictedError
import sys

pytube.request.default_range_size = 1048576  # 9MB chunk size

class Youtube2Mp3:
    def __init__(self):
        self.url: str = ""
        self.yt: YouTube = None
        self.output_path: Path = self.set_path()

    def set_path(self):
        # Find user's home directory and create youtube2mp3 directory
        # in ~/Music/youtube2mp3/ , downloaded mp3 files are saved here
        # TODO: maybe downloads belong in ~/Music instead of ~/Downloads?
        home = pathlib.Path.home()
        output_path = pathlib.Path(f"{home}/Downloads/youtube2mp3")
        
        if not pathlib.Path.exists(output_path):
            # TODO: maybe print here that we made this directory
            output_path.mkdir(parents=True, exist_ok=True)

        return output_path
        
    
    def get_youtube_video(self):
        """Takes a URL input from the user to construct a YouTube object

        Returns:
            YouTube: a YouTube video object
        """

        # get the url from the user to create YouTube object
        while True:
            try:
                self.url = yt2mp3_prompt("Enter the URL of the video to convert: ")
                self.yt = YouTube(self.url)
                self.yt.bypass_age_gate()
                break
            except Exception as e:
                yt2mp3_print(
                f"[ERROR] when retrieving URL: {e}"
                )
                continue
            
        # confirm this is the right video to convert
        while True:
            yt2mp3_print(f"'{self.yt.title}' was found")
            choice = yt2mp3_confirm(f"Is this the right video to convert")
            if choice:
                self.convert_to_mp3()
                break
            else:
                self.get_youtube_video()
            

    def convert_to_mp3(self):
        # sanitize the youtube title for the download
        # thanks to SO answer (https://stackoverflow.com/a/7406369/1327508)
        keepcharacters = (' ','.','_')
        safe_title = "".join(c for c in self.yt.title if c.isalnum() or c in keepcharacters).rstrip()
        
        # extract audio stream from the top result youtube video
        # and download to youtube2mp3/ as an mp4 initially
        yt2mp3_print("Beginning video download...")
        with ProgressBar(total=self.yt.streams.get_audio_only().filesize, unit='B', unit_scale=True) as pbar:
            pbar.set_description("yt2mp3  - Downloading video")
            self.yt.register_on_progress_callback(progress_wrapper(pbar))
            # self.yt.register_on_complete_callback(complete_function)
            self.yt.streams.get_audio_only().download(
                output_path=self.output_path,
                filename=f"{safe_title}.mp4"
            )
            
        if pathlib.Path.exists(Path(f"{self.output_path}/{safe_title}.mp4")):
            yt2mp3_print("Beginning conversion to mp3...")

        # # write final audio file as an mp3
        moviepy_audio = AudioFileClip(os.path.join(f"{self.output_path}/{safe_title}.mp4"))
        moviepy_audio.write_audiofile(os.path.join(f"{self.output_path}/{safe_title}.mp3"))
